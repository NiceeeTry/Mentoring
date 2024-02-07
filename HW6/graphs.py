from collections import deque

def bfs(graph, A, B):
    visited = set()
    search_queue = deque(A)
    while search_queue:
        # print(search_queue)
        elem = search_queue.popleft()
        if elem not in visited:
            visited.add(elem)
            search_queue.extend(graph[elem])
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



# Top sort from Geek for Geeks
from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Print contents of stack
        print (stack)
 
g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
#This code is contributed by Neelam Yadav
