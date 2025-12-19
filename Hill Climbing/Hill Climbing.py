import copy

goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_zero(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def hill_climbing(start):
    current = start
    while True:
        h_current = heuristic(current)
        if h_current == 0:
            return current

        next_states = neighbors(current)
        next_state = min(next_states, key=heuristic)

        if heuristic(next_state) >= h_current:
            return current

        current = next_state

start = [[1, 0, 3],
         [8, 2, 4],
         [7, 6, 5]]

result = hill_climbing(start)
for row in result:
    print(row)