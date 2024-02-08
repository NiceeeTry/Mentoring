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


# Does the cycle have to go through the edge?  
def is_cyclic(v, visited, finish, target, graph):
        visited.add(v)
        finish.add(v)

        for neighbour in graph[v]:
            if neighbour not in visited:
                if is_cyclic(neighbour, visited, finish, target, graph):
                    return True
            elif neighbour in finish or neighbour == target:
                return True

        finish.add(v)
        return False


def is_cyclic_edges(u, v, graph):
        visited = set()
        finish = set()
        return is_cyclic(u, visited, finish, v, graph)


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

    #Testing is_cyclic_edges
    graph = {
        '5':['2', '0'],
        '2':['3'],
        '3':['1'],
        '1':['5'],
        '4':['0', '1'],
        '0':[]
    }
    assert is_cyclic_edges('4','0', graph) == True

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
print(is_cyclic_unordered(gr2))
show_cycle_unordered(gr2)