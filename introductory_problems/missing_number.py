
def find_missing(n, arr):
	_sum = sum(arr)
	actual_sum = (n*(n+1)) //2
	return actual_sum - _sum

if __name__ == "__main__":
	n = int(input())
	arr = input()
	arr = arr.split(" ")
	arr = [int(x) for x in arr]
	print(find_missing(n, arr))
