
import heapq

goal_state = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))


def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x = (value - 1) // 3
                y = (value - 1) % 3
                distance += abs(i - x) + abs(j - y)
    return distance


def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def a_star(start):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal_state:
            return parent, current

        for neighbor in get_neighbors(current):
            new_g = g_cost[current] + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + manhattan(neighbor)
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None, None


def print_path(parent, current):
    path = []
    while current:
        path.append(current)
        current = parent[current]

    path.reverse()
    for step in path:
        for row in step:
            print(row)
        print("------")


start_state = ((1, 2, 3),
               (4, 0, 5),
               (6, 7, 8))

parent, goal = a_star(start_state)
print_path(parent, goal)