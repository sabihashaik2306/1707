from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    q = deque()
    
    # Initial state (0,0)
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        # If target found
        if x == target or y == target:
            print("Solution found!")
            print(f"Jug1: {x}, Jug2: {y}")
            return True
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        print(f"Visited: Jug1={x}, Jug2={y}")
        
        # Possible next states:
        next_states = [
            (jug1, y),      # Fill Jug1
            (x, jug2),      # Fill Jug2
            (0, y),         # Empty Jug1
            (x, 0),         # Empty Jug2
            # Pour Jug1 -> Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            # Pour Jug2 -> Jug1
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]
        
        for state in next_states:
            if state not in visited:
                q.append(state)
    
    print("No solution possible.")
    return False


if __name__ == "__main__":
    jug1 = 4   # Capacity of Jug1
    jug2 = 3   # Capacity of Jug2
    target = 2 # Target amount
    
    water_jug_bfs(jug1, jug2, target)
