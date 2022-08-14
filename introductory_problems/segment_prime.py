from functools import lru_cache
import math

@lru_cache
def is_prime(number):
    num = int(number)
    if num == 1:
        return False
    flag = False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    return not flag

@lru_cache
def get_split_count(index, number):
    if index >= len(number):
        return 1
    if number[index] == "0":
        return math.inf
    count = math.inf
    for i in range(0, 6):
        if index + i < len(number):
            prefix = number[index: index+i+1]
            if is_prime(prefix):
                count = 1 + min(count, get_split_count(index+i+1, number))
    return count




if __name__ == "__main__":
    number = input("Enter Number to Split: ")
    count = get_split_count(0, number)
    print(f"The number can be split in {count-1} ways")

