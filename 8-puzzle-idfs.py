def dfs(src, target, limit, visited_states):
    if src == target:
        return True

    if(limit <= 0):
        return False

    visited_states.append(src)

    poss_moves = possible_moves(src, visited_states)

    for move in poss_moves:
        if dfs(move, target, limit-1, visited_states):
            return True
    return False


def possible_moves(state, visited_state):
    b = state.index(-1)

    d = []
    if b not in [0, 1, 2]:
        d.append('u')
    if b not in [6, 7, 8]:
        d.append('d')
    if b not in [0, 3, 6]:
        d.append('l')
    if b not in [2, 5, 8]:
        d.append('r')

    poss_moves_to_do = []

    for i in d:
        poss_moves_to_do.append(gen(state, i, b))

    return (move_it_can for move_it_can in poss_moves_to_do
            if move_it_can not in visited_state)


def gen(state, m, b):
    temp = state.copy()

    if m == 'd':
        temp[b+3], temp[b] = temp[b], temp[b+3]

    if m == 'u':
        temp[b-3], temp[b] = temp[b], temp[b-3]

    if m == 'l':
        temp[b-1], temp[b] = temp[b], temp[b-1]

    if m == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]

    return temp


def iddfs(src, target, depth):
    visited_states = []
    for i in range(1, depth+1):
        if dfs(src, target, i, visited_states):
            return i
    return -1


src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]
depth = 1

value = iddfs(src, target, depth)
if value != -1:
    print(value, True)
else:
    print(False)
