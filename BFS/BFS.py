from collections import deque

def print_state(state):
    for row in state:
        print(row)
    print("-----")

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def bfs(start, goal):
    queue = deque()
    visited = set()

    queue.append((start, [start]))

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        visited.add(tuple(map(tuple, current)))

        for neighbor in get_neighbors(current):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Start & Goal
start_state = [
    [2, 8, 3],
    [1, 0, 4],
    [7, 6, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution = bfs(start_state, goal_state)

if solution:
    print("Number of steps:", len(solution) - 1)
    for step in solution:
        print_state(step)
else:
    print("No solution found")