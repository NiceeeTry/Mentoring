from collections import deque

def bfs(graph, A, B):
    visited = set()
    search_queue = deque(A)
    while search_queue:
        # print(search_queue)
        elem = search_queue.popleft()
        if elem not in visited:
            visited.add(elem)
            for v in graph[elem]:
                if v not in visited:
                    search_queue.append(v)
            if elem in B:
                return True
    return False


def dfs(graph, node, visited=None,): 
    if visited is None:
        visited = set()
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(graph, neighbour, visited)



def top_sort(graph):
    top_sorted = []
    visited = set()

    def dfs(graph, node, visited):
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(graph, neighbour, visited)

        top_sorted.append(node)

    for v in graph:
        if v not in visited:
            dfs(graph, v, visited)
    return top_sorted


def test():
    # Testing BFS
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1, 4, 5],
        4: [3],
        5: [3],
        6: [7],
        7: [6]
    }
    A = {0, 2} 
    B = {4, 5}
    assert bfs(graph, A, B) == True

    # Testing top_sort
    graph = {
        '5':['2', '0'],
        '2':['3'],
        '3':['1'],
        '1':[],
        '4':['0', '1'],
        '0':[]
    }
    assert top_sort(graph) == ['1', '3', '2', '0', '5', '4']

test()

from collections import defaultdict

# Cycle in ordered graph
def is_cyclic_ordered(graph):
    visited = defaultdict(int)
    def dfs(v, visited):
        visited[v] = 1
        for u in graph[v]:
            if visited[u] == 0:
                if dfs(u, visited):
                    return True
            elif visited[u] == 1:
                return True
        
        visited[v] = 2
        return False

    for v in graph:
        if dfs(v, visited):
            return True
    return False

# Show nodes of cycle in ordered graph
def show_cycle_ordered(graph):
    visited = defaultdict(int)
    parent = defaultdict(str)
    path = []

    def dfs(v, visited, parent, path):
        visited[v] = 1
        for u in graph[v]:
            if visited[u] == 0:
                parent[u] = v
                dfs(u, visited, parent, path)
                if len(path)>0:
                    return
            elif visited[u] == 1 and len(path)==0:
                parent[u] = v
                path = get_cycle(parent, u)
                print(path)
                return
        
        visited[v] = 2
    
    def get_cycle(parent, last_vertex):
        cycle = [last_vertex]
        v = parent[last_vertex]
        while v != last_vertex:
            cycle.append(v)
            v = parent[v]
        return cycle[::-1]


    for v in graph:
        dfs(v, visited, parent, path)


# Cycle in unordered graph
def is_cyclic_unordered(graph):
    visited = defaultdict(int)
    finish = defaultdict(int)
    
    def dfs(v, visited, finish, parent):
        visited[v] = 1
        for u in graph[v]:
            if u == parent:
                continue
            elif u not in visited:
                if dfs(u, visited, finish, v):
                    return True
            elif visited[u] == 1:
                return True
        
        finish[v] = 2
        return False
    
    for v in graph:
        if dfs(v, visited, finish, None):
            return True
        return False
        

# Show nodes of cycle in unordered graph
def show_cycle_unordered(graph):
    visited = defaultdict(int)
    parent = defaultdict(str)
    path = []

    def dfs(v, visited, parent, path):
        visited[v] = 1
        for u in graph[v]:
            if u == parent[v]:
                continue
            elif visited[u] == 0:
                parent[u] = v
                dfs(u, visited, parent, path)
                if len(path)>0:
                    return
            elif visited[u] == 1 and len(path)==0:
                parent[u] = v
                path = get_cycle(parent, u)
                print(path)
                return
        
        visited[v] = 2
    
    def get_cycle(parent, last_vertex):
        cycle = [last_vertex]
        v = parent[last_vertex]
        while v != last_vertex:
            cycle.append(v)
            v = parent[v]
        return cycle[::-1]


    for v in graph:
        dfs(v, visited, parent, path)


graph = {
        '5':['2', '0'],
        '2':['3'],
        '3':['1'],
        '1':[],
        '4':['0', '1'],
        '0':[]
    }
gr = {
    '2':['1'],
    '1':['2']
}
gr2 = {
    '1':['2', '3'],
    '2':['1', '4'],
    '3':['1', '4'],
    '4':['2', '3']
}
# print(is_cyclic_unordered(gr2))
# show_cycle_unordered(gr2)

# Cycle in unordered graph with given edge
def find_cycle_through_edge(graph, edge):
    def dfs(graph, start, target, visited):
        if start == target:
            return True
        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                if dfs(graph, neighbor, target, visited):
                    return True
        return False

    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])
    
    visited = set()
    cycle_exists = dfs(graph, edge[0], edge[1], visited)
 
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    
    return cycle_exists

graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['b', 'c']
}
graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a'],
    'd': ['b']
}

edge = ('a', 'b')

# cycle_exists = find_cycle_through_edge(graph, edge)
# print(cycle_exists)

def find_cycle_through_vertex(graph, v):
    visisted = set()

    def dfs(v, target, visited, parent):
        visited.add(v)
        for u in graph[v]:
            if u == parent:
                continue
            elif u not in visited:
                if dfs(u, target, visited, v):
                    return True
            elif u == target:
                return True

        return False


    return dfs(v, v, visisted, None)

graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e'],
    'e': ['b', 'c', 'd']
}
# graph = {
#     'a': ['b', 'c'],
#     'b': ['a', 'd'],
#     'c': ['a'],
#     'd': ['b']
# }

start_vertex = 'a'

# print(find_cycle_through_vertex(graph, start_vertex))



def hamiltonian_path(graph):
    top_sorted = top_sort(graph)[::-1]

    for i in range(len(top_sorted) - 1):
        if top_sorted[i+1] not in graph[top_sorted[i]]:
            return False
    return True


graph = {
    'a': ['b'],
    'b': ['c'],
    'c': ['d'],
    'd': []
}

# print(hamiltonian_path(graph))


def unique_top_sort(graph):
    degree = defaultdict(int)
    # if first u is the enterence?
    for u in graph:
        for v in graph[u]:
            degree[v] += 1
    print(degree)
    queue = deque()  
    for u in degree:
        if degree[u] == 0:
            queue.append(u)

    count_visited = 0  
    while queue:
        if len(queue) > 1:
            return False  
        u = queue.popleft()
        count_visited += 1

        for v in graph[u]:
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)

    return count_visited == len(graph)  

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}
graph = {
        '5':['2', '0'],
        '2':['3'],
        '3':['1'],
        '1':[],
        '4':['0', '1'],
        '0':[]
    }

from collections import deque

def two_color(graph):
    color = {}  
    for start_node in graph:
        if start_node not in color: 
            queue = deque([start_node])
            color[start_node] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[neighbor] == color[node]: 
                            return False
                    else:
                        color[neighbor] = 1 - color[node]  
                        queue.append(neighbor)
    return True

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

# print(two_color)

def is_valid(graph, colors):
    for node in graph:
        for neighbor in graph[node]:
            if colors[node] == colors[neighbor]:
                return False
    return True

def color_graph(graph, max_colors):
    n = len(graph)
    for i in range(max_colors**n):
        colors = [0] * n
        temp = i
        for j in range(n):
            colors[j] = temp % max_colors
            temp //= max_colors
        if is_valid(graph, colors):
            return True, colors
    return False, None

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

max_colors = 4  # Максимальное количество цветов

can_color, colors = color_graph(graph, max_colors)
if can_color:
    print("Можно раскрасить в 4 цвета. Один из вариантов раскраски:", colors)
else:
    print("Нельзя раскрасить в 4 цвета.")
