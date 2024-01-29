from functions import *
import copy

# constants
isGameOver = False
boardSize = 4

# board init
board = []
for i in range(boardSize):
    cur_row = []
    for j in range(boardSize):
        cur_row.append(0)
    board.append(cur_row)

# fill the board with two random values
numToStart = 2
while numToStart>0:
    row = random.randint(0, boardSize-1)
    col = random.randint(0, boardSize-1)

    if board[row][col] ==0:
        board[row][col] = pick_value()
        numToStart -=1

print("Welcome to Game 2048! Your goal is to combine values to get the number 2048, by merging the board in different directions. For each move, you can tpe 'w','s','a', or 'd' to merge up, down, left, or right. Other inputs would be invalid and you need to try again. If you cannot move anymore, you lose. Here's your starting board:")
display_board(board)

while not isGameOver:
    try:
        move = input("Which way do you want to merge?")
        tempBoard = copy.deepcopy(board)

        if move == "w":
            board = merge_all_up(board)
        elif move == "s":
            board = merge_all_down(board)
        elif move == "a":
            board = merge_all_left(board)
        elif move == "d":
            board = merge_all_right(board)
        else:
            raise ValueError("Invalid input. Please use 'w', 'a', 's', or 'd'.")

        if board == tempBoard:
            print("Nothing can be moved. Try a different direction!")
        else:
            if won(board):
                display_board(board)
                print("Congratulations! You win the game!")
                isGameOver = True
            else:
                generate_newVal(board)
                display_board(board)

                if cannotMove(board):
                    print("There is no possible move. You have lost the Game.")
                    isGameOver = True

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break

