from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()
    open_set.put((0, start))
    
    came_from = {}
    g_score = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    g_score[start] = 0
    
    f_score = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    f_score[start] = heuristic(start, end)
    
    while not open_set.empty():
        current = open_set.get()[1]
        
        if current == end:
            
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        for dx, dy in neighbors:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_score[current] + 1
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                    open_set.put((f_score[neighbor], neighbor))
    
    return None  


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = a_star(grid, start, end)
if path:
    print("Path (down-wise):")
    for step in path:
        print(step)
else:
    print("No path found")
