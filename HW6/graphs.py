from collections import deque
def bfs(graph, A, B):
    visited = set()
    search_queue = deque(A)
    while search_queue:
        print(search_queue)
        elem = search_queue.popleft()
        if elem not in visited:
            visited.add(elem)
            search_queue.extend(graph[elem])
            if elem in B:
                return True
    return False

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

# path_exists = bfs(graph, A, B)
# print(path_exists)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 
def dfs(graph, node, visited=None,): 
    if visited is None:
        visited = set()
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(graph, neighbour, visited)

graph = {
    '5':['2', '0'],
    '2':['3'],
    '3':['1'],
    '1':[],
    '4':['0', '1'],
    '0':[]
}

# dfs(graph, '5', visited)

def top_sort():
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
# print(top_sort('5'))


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
            

print(top_sort())