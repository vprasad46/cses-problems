def weird_algo(n):
    result = ""
    while n != 1:
        result += f"{n} "
        if n%2:
            n = n*3 + 1
        else:
            n//= 2
    print(result+"1")

if __name__ == "__main__":
    n = input()
    weird_algo(int(n))
