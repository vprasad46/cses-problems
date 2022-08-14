



if __name__ == "__main__":
    t = int(input())
    inp = []
    while t:
        row, col = [int(x) for x in input().split(" ")]
        inp.append((row,col))
        t -= 1
    for row, col in inp:
        if col > row and col % 2 != 0:
            print(col ** 2 - row + 1)
        elif col > row and col % 2 == 0:
            print((col ** 2) - (col - 1) - (col - row))
        elif row >= col and row % 2 == 0:
            print(row ** 2 - col + 1)
        elif row >= col and row % 2 != 0:
            print((row ** 2) - (row - 1) - (row - col))
            
            



