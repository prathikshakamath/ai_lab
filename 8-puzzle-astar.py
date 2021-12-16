def print_b(src):
    state = src.copy()
    state[state.index(-1)] = " "
    print(f"""
    {state[0]} {state[1]} {state[2]}
    {state[3]} {state[4]} {state[5]} 
    {state[6]} {state[7]} {state[8]} 
     """)


def h(state, target):
    count = 0
    for j in range(0, len(state)):
        if state[j] != target[j]:
            count = count+1
    # print(count)
    return count


def astar(state, target):
    states = []
    states.append(state)
    print(states)
    # states.append(src)
    g = 0
    visited_states = []
    while len(states):
        print(f"level:{g}")
        moves = []
        for state in states:
            visited_states.append(state)
            print_b(state)
            if state == target:
                print("Success")
                return
            moves += [move for move in possible_moves(
                state, visited_states) if move not in moves]
        costs = [g + h(move, target) for move in moves]
        states = [moves[i]
                  for i in range(len(moves)) if costs[i] == min(costs)]
        g += 1
        print(states)
    print("Fail")


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


src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]

astar(src, target)
