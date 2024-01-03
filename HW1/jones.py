

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

def find_route(m, initial):
    stack = [initial]
    visited = set()
    path = []

    while stack:
        curr = stack.pop()
        path.append(curr)

        if isExit(m, curr):
            return path
        visited.add(curr)
        neighbour_points = neighbours(m, curr)

        for neighbour in neighbour_points:
            if neighbour not in visited and neighbour not in stack:
                stack.append(neighbour)
    return None

def isExit(m, pos):
    row, col = shape(m)

    x, y = pos

    return (x == 0 or x == row-1 ) or (y == 0 or y == col-1)

def escape(m, initial):
    route = find_route(m, initial)
    for pos in route:
        print_map(m, pos)
        print()

m = [[False, False, False, False],
    [False, True, False, True],
    [False, True, True, True],
    [True, False, False, False]]

n = [[False, False, False, False],
    [False, True, True, False],
    [False, True, True, False],
    [False, False, False, False]]

# print(shape(m))
# print_map(m, (2,1))
# print(neighbours(m, (2,1)))
print(find_route(m,(1,1)))
# escape(m, (1,1))