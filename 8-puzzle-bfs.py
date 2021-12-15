def bfs(src, target):
    queue = []
    # queue is a list with a single element as list
    queue.append(src)
    # print(queue)
    visited_states = []
    while len(queue) > 0:
        #source = src
        source = queue.pop(0)
        # visited_states is a list with single element as list
        visited_states.append(source)

        print(source)

        if source == target:
            print("success ")
            return
        possible_states = []
        possible_states = possible_moves(source, visited_states)

        for move in possible_states:
            if move not in visited_states and move not in queue:
                queue.append(move)
                # print(queue)


def possible_moves(state, visited_states):
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

    pos_moves_it_can = []

    for i in d:
        pos_moves_it_can.append(gen(state, i, b))

    return [move_it_can for move_it_can in pos_moves_it_can if
            move_it_can not in visited_states]


def gen(state, m, b):
    temp = state.copy()

    if m == 'd':
        temp[b+3], temp[b] = temp[b], temp[b+3]

    if m == 'u':
        temp[b-3], temp[b] = temp[b], temp[b-3]

    if m == 'l':
        temp[b - 1], temp[b] = temp[b], temp[b - 1]

    if m == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]

    return temp


src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]

bfs(src, target)
