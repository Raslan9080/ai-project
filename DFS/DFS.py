from collections import deque

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

MOVES = {
    "UP": -3,
    "DOWN": 3,
    "LEFT": -1,
    "RIGHT": 1
}

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = zero_index // 3, zero_index % 3

    for move, delta in MOVES.items():
        new_index = zero_index + delta

        if move == "UP" and row == 0:
            continue
        if move == "DOWN" and row == 2:
            continue
        if move == "LEFT" and col == 0:
            continue
        if move == "RIGHT" and col == 2:
            continue

        new_state = list(state)
        new_state[zero_index], new_state[new_index] = \
            new_state[new_index], new_state[zero_index]

        neighbors.append(tuple(new_state))

    return neighbors


def dfs(start_state):
    stack = [(start_state, [start_state])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == GOAL_STATE:
            return path

        if state not in visited:
            visited.add(state)

            for neighbor in get_neighbors(state):
                stack.append((neighbor, path + [neighbor]))

    return None

start_state = (1, 2, 3,
               4, 5, 0,
               6, 7, 8)

solution = dfs(start_state)

if solution:
    print(f"Solution found in {len(solution)-1} moves:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print("------")
else:
    print("No solution found")
