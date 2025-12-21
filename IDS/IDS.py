# 8-Puzzle using Iterative Deepening Search (IDS)

# Goal State
GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Possible moves: Up, Down, Left, Right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_zero(state):
    """Find position of 0 (empty tile)"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def is_goal(state):
    """Check if current state is goal"""
    return state == GOAL_STATE


def get_neighbors(state):
    """Generate all valid neighboring states"""
    neighbors = []
    x, y = find_zero(state)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Convert tuple to list to swap
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def depth_limited_dfs(state, depth, visited, path):
    """Depth Limited DFS"""
    if is_goal(state):
        return path

    if depth == 0:
        return None

    visited.add(state)

    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_dfs(
                neighbor,
                depth - 1,
                visited,
                path + [neighbor]
            )
            if result is not None:
                return result

    visited.remove(state)
    return None


def ids(start_state, max_depth):
    """Iterative Deepening Search"""
    for depth in range(max_depth + 1):
        visited = set()
        result = depth_limited_dfs(start_state, depth, visited, [start_state])
        if result is not None:
            return result
    return None




if name == "main":
    initial_state = (
        (1, 2, 3),
        (4, 5, 0),
        (6, 7, 8)
    )

    solution = ids(initial_state, max_depth=20)

    if solution:
        print("Solution found!\n")
        for step in solution:
            for row in step:
                print(row)
            print("-----")
    else:
        print("No solution found.")