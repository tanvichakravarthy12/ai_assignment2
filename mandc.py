from collections import deque

def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False
    if (M_left > 0 and C_left > M_left):
        return False
    if (M_right > 0 and C_right > M_right):
        return False

    return True

def get_successors(state):
    M, C, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    successors = []

    for m, c in moves:
        if boat == 1:
            new_state = (M-m, C-c, 0)
        else:
            new_state = (M+m, C+c, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors

#bfs
def bfs():
    start = (3,3,1)
    goal = (0,0,0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for successor in get_successors(state):
            queue.append((successor, path + [state]))

    return None

solution = bfs()
print("BFS Solution:")
for step in solution:
    print(step)


#dfs
def dfs():
    start = (3,3,1)
    goal = (0,0,0)

    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for successor in get_successors(state):
            stack.append((successor, path + [state]))

    return None

solution = dfs()
print("DFS Solution:")
for step in solution:
    print(step)


#depth limited search (DLS)
def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left


    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False


    if M_left > 0 and C_left > M_left:
        return False


    if M_right > 0 and C_right > M_right:
        return False

    return True

def get_successors(state):
    M, C, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []

    for m, c in moves:
        if boat == 1:
            new_state = (M - m, C - c, 0)
        else:
            new_state = (M + m, C + c, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors



#depth limited search (recursive)
def dls(state, goal, depth_limit, path, visited):

    if state == goal:
        return path + [state]


    if depth_limit == 0:
        return None

    visited.add(state)

    for successor in get_successors(state):
        if successor not in visited:
            result = dls(successor,
                         goal,
                         depth_limit - 1,
                         path + [state],
                         visited)
            if result:
                return result

    return None

def run_dls(depth_limit):
    start = (3, 3, 1)
    goal = (0, 0, 0)

    visited = set()
    solution = dls(start, goal, depth_limit, [], visited)

    if solution:
        print("Solution found within depth limit:", depth_limit)
        for step in solution:
            print(step)
    else:
        print("No solution found within depth limit:", depth_limit)

if __name__ == "__main__":
    depth = 11
    run_dls(depth)


#iterative deepening DFS (IDDFS)
def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left


    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False


    if M_left > 0 and C_left > M_left:
        return False


    if M_right > 0 and C_right > M_right:
        return False

    return True

def get_successors(state):
    M, C, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    successors = []

    for m, c in moves:
        if boat == 1:
            new_state = (M - m, C - c, 0)
        else:
            new_state = (M + m, C + c, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


#iterative deepening DFS
def iddfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    depth = 0

    while True:
        print("\nTrying depth limit:", depth)
        visited = set()
        result = dls(start, goal, depth, [], visited)

        if result:
            print("\nSolution found at depth:", depth)
            return result

        depth += 1

if __name__ == "__main__":
    solution = iddfs()

    print("\nFinal Solution Path:")
    for step in solution:
        print(step)



