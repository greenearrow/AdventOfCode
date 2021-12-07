## Bingo!


def play(boards, drawn):
    turns = [[[None for item in range(0, 5)] for row in range(0, 5)] for board in range(0, 100)]
    for i, draw in enumerate(drawn):
        for board in range(0, 100):
            for row in range(0, 5):
                for item in range(0, 5):
                    if draw == boards[board][row][item]:
                        turns[board][row][item] = i
    return turns
    
def find_winner(turns):
    test_2 = 1000
    board_win = []
    for board_number, board in enumerate(turns):
        board_test = 1000
        for pos in range(0,5):
            vert = []
            hori = []
            for i in range(0,5):

                vert.append(board[pos][i])
                hori.append(board[i][pos])
            if max(vert) < test_2 or max(hori) < test_2: 
                test_2 = max(vert)
                winning_board = board_number
            if min([max(vert), max(hori)]) < board_test:
                board_test = min([max(vert),max(hori)])
        board_win.append(board_test)

    winning_turn = test_2
    winning_board_number = winning_board
    return winning_board_number, winning_turn, board_win

def find_loser(turns):
    '''find win on each board (first row or column to match 5)'''
    test_2 = 0
    for board_number, board in enumerate(turns):
        for row_number in range(0,5):
            for item_number in range(0,5): pass


def score(winning_board, winning_turns, winning_turn, drawn):
    my_score = 0
    for row in range(0,5):
        for item in range(0,5):
            if winning_turns[row][item] > winning_turn:
                my_score += drawn[winning_turn] * winning_board[row][item]
    return my_score

def question_1(drawn, boards):
    turns = play(boards, drawn)
    winning_board_number, winning_turn, _ = find_winner(turns)
    winning_board = boards[winning_board_number]
    winning_turns = turns[winning_board_number]
    my_score = score(winning_board, winning_turns, winning_turn, drawn)
    return my_score

def question_2(drawn, boards):
    turns = play(boards, drawn)
    _, _, board_win = find_winner(turns)
    losing_board_number = board_win.index(max(board_win))
    losing_board = boards[losing_board_number]
    losing_turn = board_win[losing_board_number]
    losing_turns = turns[losing_board_number]

    my_score = score(losing_board, losing_turns, losing_turn, drawn)
    return my_score

if __name__ == '__main__':
    with open(r'data/day_4_drawn.txt') as f1:
        drawn = f1.read().split(',')
    drawn = [int(item) for item in drawn]
    with open(r'data/day_4_board.txt') as f2:
        boards = [[[int(item) for item in row.split(' ') if item != ''] for row in board.split('\n')] for board in f2.read().split('\n\n')]
    print(question_1(drawn,boards))
    print(question_2(drawn,boards))
