from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    print("BFS Traversal:", end=" ")
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])  

    print() 
if __name__ == "__main__":
  
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    bfs(graph, 'A')
