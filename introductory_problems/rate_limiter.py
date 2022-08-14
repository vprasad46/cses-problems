import time


max_requests_per_second = 10
customer_reqs = dict()
max_carry_over = 10

def refill(customer_id):
    global max_requests_per_second, unit_req_count, customer_reqs, max_carry_over
    last_timestamp = customer_reqs[customer_id]["last_timestamp"]
    now_timestamp = time.time()
    seconds_passed = now_timestamp - last_timestamp
    reqs_to_fill = min(max_requests_per_second, int(max_requests_per_second * seconds_passed))
    if reqs_to_fill == max_requests_per_second:
        customer_reqs[customer_id]['credit']  = min(max_carry_over, customer_reqs[customer_id]['credit'] + customer_reqs[customer_id]['reqs_remaining'])
    customer_reqs[customer_id]['reqs_remaining'] = min(max_requests_per_second, reqs_to_fill + customer_reqs[customer_id]['reqs_remaining'])
    customer_reqs[customer_id]['last_timestamp'] = now_timestamp

def rateLimit(customer_id):
    global customer_reqs, max_requests_per_second
    if customer_id not in customer_reqs:
        customer_reqs[customer_id] = {"last_timestamp": time.time(), "reqs_remaining": max_requests_per_second, "credit": 0}
    else:
        refill(customer_id)
    remaining_reqs = customer_reqs[customer_id]["reqs_remaining"]
    credit = customer_reqs[customer_id]["credit"]
    if remaining_reqs or credit:
        if remaining_reqs:
            customer_reqs[customer_id]["reqs_remaining"] -= 1
        elif credit:
            customer_reqs[customer_id]["credit"] -= 1
        return True
    else:
        return False
        

