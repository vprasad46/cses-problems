
from collections import deque

def get_dir(dx, dy):
    result = ""
    if dx == 0 and dy == 1:
        result = "R"
    elif dx == 1 and dy == 0:
        result = "D"
    elif dx == 0 and dy == -1:
        result = "L"
    else:
        result = "U"
    return result

def reach_destination(r, c):
    queue = deque([(r,c, "")])
    while queue:
        x, y, cur_dir = queue.popleft()
        if matrix[x][y] == "B":
            print("YES")
            print(len(cur_dir))
            print(cur_dir)
            return
        matrix[x][y] = "#"

        for pos in range(len(_DIR)-1):
            dx = _DIR[pos]
            dy = _DIR[pos+1]
            _dir = get_dir(dx, dy)
            if 0<=x+dx<rows and 0<=y+dy<cols and matrix[x+dx][y+dy] != "#":
                queue.append((x+dx, y+dy, cur_dir+_dir))

    print("NO")

if __name__ == "__main__":
    rows, cols = [int(x) for x in input().split(" ")]
    matrix = []
    _DIR = [0,1,0,-1,0]
    for r in range(rows):
        matrix.append(list(input()))
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "A":
                reach_destination(r, c)
                break

