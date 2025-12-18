import heapq

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def greedy_best_first_search(start):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start), start))
    visited = set()
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal_state:
            return parent

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(pq, (manhattan_distance(neighbor), neighbor))

    return None

# Example initial state
start_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

result = greedy_best_first_search(start_state)
print("Solution found!" if result else "No solution found.")