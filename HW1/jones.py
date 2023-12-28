

def print_map(m, pos):
    n, k = shape(m)
    for row in range(n):
        for col in range(k):
            if pos == (row,col):
                print("@", end='')
            elif m[row][col]:
                print(".", end='')
            else:
                print("#", end='')
        print()

def shape(m):
    return len(m), len(m[0])

def neighbours(m, pos):
    row, col = shape(m)
    x, y = pos
    res = []

    shift = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in shift:
        newX, newY = x + dx, y + dy
        
        if 0 <= newX < row and 0 <= newY < col and m[newX][newY]:
            res.append((newX,newY))
    return res



m = [[False, False, False, False],
    [False, True, False, True],
    [False, True, False, True],
    [True, True, False, False]]


# print(shape(m))
# print_map(m, (2,1))
print(neighbours(m, (2,1)))