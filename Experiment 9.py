from itertools import permutations


def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]] 
    return total_distance


def travelling_salesman(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_distance = float('inf')
    best_path = []

   
    for path in permutations(cities):
        current_distance = calculate_distance(path, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path

    return best_path, min_distance


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_path, min_distance = travelling_salesman(distance_matrix)
print("Best path:", best_path)
print("Minimum distance:", min_distance)
