

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

    while stack:
        curr = stack[-1]

        if isExit(m, curr):
            return stack

        neighbour_points = neighbours(m, curr)

        unvisited = [n for n in neighbour_points if n not in visited]

        if unvisited:
            next_to_visit = unvisited[0]
            stack.append(next_to_visit)
            visited.add(next_to_visit)
        else:
            stack.pop()
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
    [False, True, False, True],
    [True, True, False, False]]

n = [[False, False, False, False],
    [False, True, True, False],
    [False, True, True, False],
    [False, False, False, False]]

# print(shape(m))
# print_map(m, (2,1))
# print(neighbours(m, (2,1)))
# print(find_route(n,(1,1)))
escape(m, (1,1))