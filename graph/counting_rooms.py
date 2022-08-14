from collections import deque

def mark_room(matrix, i, j):
    st = time.time()
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        matrix[x][y] = "#"
        for pos in range(len(_DIR)-1):
            dx = _DIR[pos]
            dy = _DIR[pos+1]
            if 0<=x+dx<len(matrix) and 0<=y+dy<len(matrix[0]) and matrix[x+dx][y+dy] == ".":
                queue.append((x+dx, y+dy))

def display(matrix):
    for r in range(len(matrix)):
        x = ""
        for c in range(len(matrix[0])):
            x += " " + matrix[r][c]
        print(x)


if __name__ == "__main__":
    rows, cols = [int(x) for x in input().split(" ")]
    _DIR = [0,1,0,-1,0]
    matrix = []
    for row in range(rows):
        matrix.append(list(input()))

    rooms = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == ".":
                rooms += 1
                mark_room(matrix, i, j)
    print(rooms)
