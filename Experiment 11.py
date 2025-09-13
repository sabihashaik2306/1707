
def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def map_coloring(graph, colors, assignment={}, region=0):
    if region == len(graph):
        return assignment 
    
    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color
            result = map_coloring(graph, colors, assignment, region+1)
            if result:
                return result
            assignment.pop(region)  
    return None


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors = ['Red', 'Green', 'Blue']

solution = map_coloring(graph, colors)

if solution:
    print("Coloring of regions:")
    for region, color in solution.items():
        print(f"Region {region}: {color}")
else:
    print("No solution found")
