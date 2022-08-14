def get_max_pages():
    dp = []
    for _ in range(2):
        temp = []
        for _ in range(x+1):
            temp.append(0)
        dp.append(temp)

    for book in range(1, len(prices)+1):
        for amount in range(1, x+1):
            if amount >= prices[book-1]:
                dp[1][amount] = max(dp[0][amount], pages[book-1] + dp[0][amount-prices[book-1]])
            else:
                dp[1][amount] = dp[0][amount]

        temp = [0] * (x+1)
        dp[0] = dp[1]
        dp[1] = temp
    return dp[0][-1]
 
if __name__ == "__main__":
    n, x = [int(x) for x in input().split(" ")]
    prices = input()
    prices = [int(x) for x in prices.split(" ")]
    pages = input()
    pages = [int(x) for x in pages.split(" ")]
    print(get_max_pages())
