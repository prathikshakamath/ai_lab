import random as r


def init():
    global ai, player, board, weights
    ai, player = 'O', 'X'
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    weights = [[3, 2, 3],
               [2, 4, 2],
               [3, 2, 3]]


def move(row, col, ch):
    if board[row][col] == '_':
        board[row][col] = ch
        weights[row][col] = 0
        return True
    else:
        return False


def display(move_type='board'):
    if move_type == 'ai':
        print("**AI**")
    elif move_type == 'board':
        print("**Board of Tic-tac-Toe**")
    else:
        print("**Player Move**")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end='\t')
        print('\n')
    print('\n')


def get_position():
    max_value = max([max(x) for x in weights])
    positions = [(i, weights[i].index(max_value)) for i in range(3)
                 if max_value in weights[i]]
    return positions


def has_tied():
    for row in board:
        if '_' in row:
            return False
    return True


def compare_line(s1, ch):
    return '_' in s1 and s1.count(ch) == 2


def attacking_position(ch):
    default = '_'
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        # checking for each row
        if compare_line(board[i], ch):
            return(i, board[i].index(default))
        elif compare_line(col, ch):
            return(col.index(default), i)
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if compare_line(diag1, ch):
        return (diag1.index(default), diag1.index(default))
    elif compare_line(diag2, ch):
        return (diag2.index(default), 2-diag2.index(default))
    return False


def ai_move():
    global ai, player
    pos, f = attacking_position(ch=ai), False
    if pos != False:
        row, col = pos
        f = True
    else:
        pos = attacking_position(ch=player)
        if pos != False:
            row, col = pos
        else:
            row, col = r.choice(get_position())
    move(row, col, ai)
    return f


def run():
    global ai, player
    end, tied, move_type = False, False, None
    print('*'*10+"Tic-Tac-Toe"+'*'*10)
    display()
    ch = input('Choose a character X or O: ')
    if ch == 'O':
        ai, player = player, ai
    while(True):
        if tied:
            print('The match is tied')
            return
        elif end:
            print(move_type+' has won')
            return
        move_type = 'player'
        r = int(input("Enter row:"))
        c = int(input("Enter column:"))
        if not move(r-1, c-1, player):
            print('Enter valid position!')
        else:
            display(move_type=move_type)
            tied = has_tied()
            if tied:
                continue
            move_type = 'ai'
            end = ai_move()
            display('ai')
            tied = has_tied()


def main():
    init()
    run()
    f = 'Y'
    while(f == 'Y' or f == 'y'):
        f = input("Do you want to play again Y or N")
        init()
        if f == 'Y' or f == 'y':
            run()
    print('\n Thankyou')


main()
