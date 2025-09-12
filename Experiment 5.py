from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    """Check if a state is valid (missionaries never outnumbered)."""
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def missionaries_cannibals():
    start = (3, 3, 0, 0, 1)  
    goal = (0, 0, 3, 3, 0)
    
    queue = deque([(start, [])]) 
    visited = set()
    
    while queue:
        (m_left, c_left, m_right, c_right, boat), path = queue.popleft()
        
        if (m_left, c_left, m_right, c_right, boat) in visited:
            continue
        visited.add((m_left, c_left, m_right, c_right, boat))
        
        if (m_left, c_left, m_right, c_right, boat) == goal:
            print("Solution found!\n")
            for step in path + [goal]:
                print(step)
            return
        
     
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        
        for m, c in moves:
            if boat == 1:  
                new_state = (m_left - m, c_left - c,
                             m_right + m, c_right + c, 0)
            else:  
                new_state = (m_left + m, c_left + c,
                             m_right - m, c_right - c, 1)
            
            if is_valid(*new_state[:4]):
                queue.append((new_state, path + [(m_left, c_left, m_right, c_right, boat)]))
    
    print("No solution exists.")

if __name__ == "__main__":
    missionaries_cannibals()
