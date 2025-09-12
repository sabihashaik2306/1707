import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.zero_pos = board.index(0)  # Blank space position

    def __lt__(self, other):
        return (self.cost + self.depth) < (other.cost + other.depth)

    def generate_children(self):
        children = []
        x, y = divmod(self.zero_pos, 3)
        directions = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1),
        }
        for move, (nx, ny) in directions.items():
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_board = self.board[:]
                new_board[self.zero_pos], new_board[new_pos] = new_board[new_pos], new_board[self.zero_pos]
                children.append(PuzzleState(new_board, self, move, self.depth + 1))
        return children

    def manhattan_distance(self, goal):
        distance = 0
        for i, value in enumerate(self.board):
            if value != 0:
                goal_index = goal.index(value)
                x1, y1 = divmod(i, 3)
                x2, y2 = divmod(goal_index, 3)
                distance += abs(x1 - x2) + abs(y1 - y2)
        return distance


def a_star(start, goal):
    open_list = []
    closed_set = set()
    start_state = PuzzleState(start)
    start_state.cost = start_state.manhattan_distance(goal)
    heapq.heappush(open_list, start_state)

    while open_list:
        current = heapq.heappop(open_list)
        if current.board == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)  # include start
            return path[::-1]  # Reverse path
        closed_set.add(tuple(current.board))
        for child in current.generate_children():
            if tuple(child.board) not in closed_set:
                child.cost = child.manhattan_distance(goal)
                heapq.heappush(open_list, child)
    return None


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()


# Example usage:
if __name__ == "__main__":
    start_state = [1, 2, 3,
                   4, 0, 6,
                   7, 5, 8]   # Initial configuration
    goal_state = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 0]   # Goal configuration

    solution = a_star(start_state, goal_state)

    if solution:
        print("Solution found!\n")
        for step in solution:
            print(f"Move: {step.move if step.move else 'Start'}")
            print_board(step.board)
    else:
        print("No solution exists.")
