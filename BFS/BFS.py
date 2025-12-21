from collections import deque
import copy


def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print("-----")


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def is_solvable(start, goal):
    def count_inversions(puzzle):
        flat = [num for row in puzzle for num in row if num != 0] 
        inv = 0
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inv += 1
        return inv

    inv_start = count_inversions(start)
    inv_goal = count_inversions(goal)
    return (inv_start % 2) == (inv_goal % 2)


def bfs(start, goal):
    queue = deque()
    queue.append((start, [start])) 
    visited = set()

    while queue:
        current_state, path = queue.popleft()

      
        state_tuple = tuple(tuple(row) for row in current_state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current_state == goal:
            return path

        for neighbor in get_neighbors(current_state):
            queue.append((neighbor, path + [neighbor]))

    return None


start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]


goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]



print("التحقق من إمكانية الحل...")
if not is_solvable(start_state, goal_state):
    print("هذا اللغز مستحيل الحل! (عدد الانقلابات مختلف الـ parity)")
else:
    print("اللغز قابل للحل، جاري البحث عن الحل...")
    solution = bfs(start_state, goal_state)

    if solution:
        print(f"تم العثور على الحل في {len(solution) - 1} خطوة!")
        print("\nالخطوات:")
        for step in solution:
            print_state(step)
    else:
        print("لم يتم العثور على حل (لكن هذا غير متوقع إذا كان solvable)")