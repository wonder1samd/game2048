import random
import copy

boardSize = 4

def display_board(board):
    for row in board:
        cur_row = "|"
        for element in row:
            if element == 0:
                cur_row += " |"
            else:
                cur_row+=str(element) + "|"
        print(cur_row)

def  merge_row_left(row):
    for j in range(boardSize-1):
        for i in range(boardSize-1,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    
    for i in range(boardSize-1):
        if row[i] == row[i+1]:
            row[i]*=2
            row[i+1]=0
    
    for i in range(boardSize-1,0,-1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    return row

def merge_all_left(board):
    for i in range(boardSize):
        board[i] = merge_row_left(board[i])
    return board

def reverse(row):
    new_row = []
    for i in range(boardSize-1,-1,-1):
        new_row.append(row[i])
    return new_row

def merge_all_right(board):
    for i in range(boardSize):
        board[i] = reverse(board[i])
        board[i] = merge_row_left(board[i])
        board[i] = reverse(board[i])
    return board

def transpose(board):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i==j:
                temp = board[j][i]
                board[j][i] = board[i][j]
                board[i][j] = temp
    return board

def merge_all_up(board):
    board = transpose(board)
    board = merge_all_left(board)
    board = transpose(board)
    return board

def merge_all_down(board):
    board = transpose(board)
    board = merge_all_right(board)
    board = transpose(board)
    return board    

def pick_value():
    if random.randint(1,8) == 1:
        return 4
    else:
        return 2

def generate_newVal(board):
    row = random.randint(0, boardSize-1)
    col = random.randint(0, boardSize-1)
    while not board[row][col] == 0:
        row = random.randint(0, boardSize-1)
        col = random.randint(0, boardSize-1)      
    board[row][col] = pick_value()

def won(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def cannotMove(board):
    tempboard1 = copy.deepcopy(board)
    tempboard2 = copy.deepcopy(board)

    tempboard1 = merge_all_down(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = merge_all_up(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1 = merge_all_left(tempboard1)
            if tempboard1 == tempboard2:
                tempboard1 = merge_all_right(tempboard1)
                if tempboard1 == tempboard2:
                    return True
    return False