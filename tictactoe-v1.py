import random

# set up our board

board = [
          [ '.', '.', '.' ],
          [ '.', '.', '.' ],
          [ '.', '.', '.' ]

        ]

# display the board
def displayboard():
    for x in range(len(board)):

        # go through each column
        for y in range(len(board[x])):

            print (board[x][y], '\t', end='')

        print ()

game = True

while game == True:

    displayboard()

    # ask the user for their position
    row = int(input("Row: "))
    col = int(input("Col: "))

    # put the user's mark in that spot
    board[row][col] = 'X'

    displayboard()

    # let the computer try to pick a spot for its O
    keepgoing = True

    while keepgoing == True:

        # grab a random row & col
        rrow = random.randint(0,2)
        rcol = random.randint(0,2)

        if board[rrow][rcol] == '.':
            # put an O here
            board[rrow][rcol] = 'O'
            keepgoing = False

    print ("Computer!\n\n")
