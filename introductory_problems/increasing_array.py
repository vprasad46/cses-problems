


def min_moves(size, arr):
    moves = 0
    cur_el = arr[0]

    for i in range(1, size):
        next_el = arr[i]
        if next_el < cur_el:
            actual_next_el = cur_el
            moves += actual_next_el - next_el
            arr[i] = actual_next_el
        cur_el = arr[i]
    return moves


if __name__ == "__main__":
    size = int(input())
    arr = input()
    arr = [int(x) for x in arr.split(" ")]
    print(min_moves(size, arr))

