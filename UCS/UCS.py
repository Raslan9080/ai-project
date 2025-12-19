import heapq


initial_state = (
    (1, 2, 3),
    (4, 0, 5),
    (6, 7, 8)
)

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)


moves = [
    (0, 1, "Right"),
    (0, -1, "Left"),
    (-1, 0, "Up"),
    (1, 0, "Down")
]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_successors(state):
    successors = []
    x, y = find_blank(state)

    for dx, dy, move in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append((tuple(tuple(row) for row in new_state), move))
    return successors

def uniform_cost_search():
    pq = []
    heapq.heappush(pq, (0, initial_state, []))
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal_state:
            return cost, path + [(state, "Goal")]

        for next_state, move in generate_successors(state):
            if next_state not in visited:
                heapq.heappush(
                    pq,
                    (cost + 1, next_state, path + [(state, move)])
                )

    return None

def print_solution(solution):
    cost, steps = solution
    print("Solution Found!")
    print("Total Cost:", cost)
    print("Number of Moves:", cost)
    print("\nSteps:\n")

    for i, (state, move) in enumerate(steps):
        print(f"Step {i}: {move}")
        for row in state:
            print(row)
        print("-" * 20)


solution = uniform_cost_search()
if solution:
    print_solution(solution)
else:
    print("No solution found.")
