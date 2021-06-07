
import numpy as np

r1 = ['WR', 'WK', 'WB', 'W*', 'WQ', 'WB', 'WK', 'WR']
r2 = ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP']
r7 = ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP']
r8 = ['BR', 'BK', 'BB', 'B*', 'BQ', 'BB', 'BK', 'BR']


r3 = ["  ", "##", "  ", "##", "  ", "##", "  ", "##"]
r4 = ["##", "  ", "##", "  ", "##", "  ", "##", "  "]
r5 = ["  ", "##", "  ", "##", "  ", "##", "  ", "##"]
r6 = ["##", "  ", "##", "  ", "##", "  ", "##", "  "]
Startboard = [r1, r2, r3, r4, r5, r6, r7, r8]


Tutorial = ("Instructions to Play Chess! The white player always moves first, and players will alternate turns. One piece can be moved at a time. When another player’s piece is encountered in your path of movement, the piece will be captured. Each kind of piece has specific ways it can move…Pawns can move in one space in all directions, except backwards, and can move two spaces forward on their initial move. A knight can only move in the pattern of two horizontal steps and one square vertically or two vertical steps and one turn horizontally. The bishop can only move diagonally, and cannot move over its own team’s pieces. The rook can move horizontally or vertically, but cannot move diagonally. The Queen piece can move any number of squares in any direction during the turn, this condition makes it the most powerful piece. The King can move one space in any direction, but cannot be moved into check. A player is “in check” when their King can be attacked by one of their opponent’s pieces. To win the game, put your opponent’s king in “checkmate.” Checkmate occurs when the opponent’s king is in check, and the piece that has the King in check is unable to be captured. In addition, the check must be unable to be blocked and the King must be incapable of moving to a square that’s not actively under attack.")

#beginning board with zero-indexed index numbers
def indexed_board(board):
    print ("   0  1  2  3  4  5  6  7")
    for i in range(0, 8):
        print (str(i) + "  " + " ".join(Startboard[i]))

final_board = indexed_board(Startboard)


def opp(player):
  if player == "W":
    return "B"
  else:
    return "W"

player1 = "W"
player2 = opp(player1)
curr_player = player1


def piece(x, y):
  return Startboard[x][y]

def piece_type(x, y):
  return piece(x, y)[1]

def own_piece(input, player):
  if piece(input[0], input[1])[0]==player:
    return True
  else:
    return False

def move(board, x1, y1, x2, y2):
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = "  "

#update display function
def update_display(Board):
  Startboard = [ r1, r2, r3, r4, r5, r6, r7, r8]
  for i in range(0, 8):
   	 print (" ".join(Startboard[i]))


def is_empty(board, x, y):
    if board[x][y] == "  " or board[x][y] == "##":
        return True
    else:
        return False

#PIECE FUNCTIONS

def bishop(board, x1, y1, x2, y2):
    if abs(x1 - x2) == abs(y1 - y2):
        if x2 - x1 == 1 or x2 - x1 == -1:
            return True
        elif x1 - x2 < 1 and y1 - y2 < 1:
            for i in range(1, x2 - x1):
                if is_empty(board, x1 + i, y1 + i):
                    return True
        elif x1 - x2 > 1 and y1 - y2 > 1:
        	#UL
            for i in range(1, x1 - x2):
                if is_empty(board, x1 - i, y1 - i):
                    return True
        elif x1 - x2 < 1 and y1 - y2 > 1:
            for i in range(1, x2 - x1):
                if is_empty(board, x1 - i, y1 + i):
                    return True
        elif x1 - x2 > 1 and y1 - y2 < 1:
        	#UR
            for i in range(1, x1 - x2):
                if is_empty(board, x1 + i, y1 - i):
                    return True
    return False

def rook(board, x1, y1, x2, y2):
    if x1 == x2:
        if y1 - y2 == 1 or y1 - y2 == -1:
            return True
        if y1 - y2 < 1:
            for i in range(1, y2 - y1):
                if is_empty(board, x1, y1 + i) == False:
                    return False
            return True
        if y1 - y2 > 1:
            for i in range(1, y1 - y2):
                if is_empty(board, x1, y1 - i) == False:
                    return False
            return True
    elif y1 == y2:
        if x1 - x2 == 1 or x1 - x2 == -1:
            return True
        if x1 - x2 < 1:
            for i in range(1, x2 - x1):
                if is_empty(board, x1 + 1, y1) == False:
                    return False
            return True
        if x1 - x2 > 1:
            for i in range(1, x1 - x2):
                if is_empty(board, x1 - 1, y1) == False:
                    return False
            return True
    else:
        return False


def knight(Board, x1, y1, x2, y2):
  curr = np.array([x1, y1])
  move = [x2, y2]
  dir_list = np.array([[-2, 1], [2, 1], [-2, -1], [2, -1], [-1, -2], [1, 2], [1, -2], [-1, 2]])
  check = []
  for i in range(len(dir_list)):
    dir_change = curr+dir_list
    dir_change = dir_change.tolist()
  for i in range(len(dir_change)):
      # if dir_change[i]==move:
      if move == dir_change[i]:
          check.append('True')
      else:
          check.append('False')
  if 'True' in check:
       return True
  else:
       return False

def Wpawn(board, x1, y1, x2, y2):
    if y1 == y2:
        if x1 + 1 == x2:
            return is_empty(board, x2, y2)
        if x1 + 2 == x2:
            if is_empty(board, x1 + 1, y1):
                return is_empty(board, x2, y2)
        return False
    if y1 - 1 == y2 or y1 + 1 == y2:
        if x1 + 1 == x2:
            return not is_empty(board, x2, y2)
    return False

def Bpawn(board, x1, y1, x2, y2):
    if y1 == y2:
        if x1 - 1 == x2:
            return is_empty(board, x2, y2)
        if x1 - 2 == x2:
            if is_empty(board, x1 - 1, y1):
                return is_empty(board, x2, y2)
    if y1 - 1 == y2 or y1 + 1 == y2:
        if x1 - 1 == x2:
            return not is_empty(board, x2, y2)
    return False

def pawn(board, x1, y1, x2, y2):
    if curr_player == "W":
        return Wpawn(board, x1, y1, x2, y2)
    else:
        return Bpawn(board, x1, y1, x2, y2)

def queen(board, x1, y1, x2, y2):
    if rook(board, x1, y1, x2, y2) == True:
        return True
    if bishop(board, x1, y1, x2, y2) == True:
        return True
    return False


def king(board, x1, y1, x2, y2):
    if abs(x1 - x2) > 1 or abs(y1 - y2) > 1:
        return False
    elif piece(board, x2, y2)[0] == opponent(player)[0] or is_empty(board, x2, y2):
        return not is_check(move(board, x1, y1, x2, y2), player)
    else:
    	return False

#Functions for Making Moves

piece_dict = {"*" : king, "P": pawn, "Q" : queen, "R" : rook, "B" : bishop, "K" : knight}

def piece_move_match(board, x1, y1, x2, y2):
    # piece_dict[piece_type(current_value[0], current_value[1])](Startboard, current_value[0], current_value[1], end[0], end[1])
    return piece_dict[piece_type(x1, y1)](Startboard, x1, y1, x2, y2)
       
def find(board, piece):
    for i in range(0, 8):
        for j in range(0,8):
            if board[i][j] == piece:
                return [i, j]

#checks for valid imputs

def within_range(input):
  check_lst = list()
  for i in range(len(input)):
    if int(input[i])>=0 and int(input[i])<=7:
      check_lst.append('True')
    else:
      check_lst.append('False')
  if 'False' in check_lst:
    return False
  else:
    return True

def own_piece(input, player):
  if piece(int(input[0]), int(input[1]))[0]==player:
    return True
  else:
    return False

def validcheck_start():
    if current_value.isdigit()==False:
        return False
    elif within_range(current_value)==False:
        return False
    elif own_piece(current_value, curr_player)==False:
        return False
    else:
        return True

def validcheck_end():
    if end.isdigit()==False:
        return False
    elif within_range(end)==False:
        return False
    elif own_piece(end, curr_player)==True:
        return False
    else:
        return True

#Check and Checkmate
def is_check(board, player):
    king = find(board, str(player[0]) + "*")
    #finds position pf player's king
    for i in range(0,8):
        for j in range(0,8):
            #iterate through all spaces
            if piece(i, j)[0] == opp(player):
            #if piece in space belongs to opponent
                if piece_dict[piece(i, j)[1]](board, i, j, king[0], king[1]) == True:
                    return True
                    #stop and return True if piece can move to king's spot


def is_checkmate(board, player):
  check = []
  board2 = board[:]
  if is_check(board, player)==True:
    king = find(board, str(player[0]) + "*")
    for i in range(0, 8):
      for j in range(0, 8):
        if piece(i, j)[0]==player:
          for x in range(0, 8):
            for y in range (0,8):
              if piece_dict[piece(i, j)[1]](board, i, j, x, y) == True:
                  final_change = move(board2, i, j, x, y)
                  check.append(is_check(final_change, player))
                  if False in check:
                      return False
                  else:
                      return True
  else:
      return False   
        
#Actual Game Code

#Intro and start game

start = input("Type start or turorial to begin:  ")
valid = False
while valid == False:
    if start == "start":
        print (final_board)
        valid = True
    elif start == "tutorial":
        valid = True
        print (Tutorial)
        start = input("Type Start to begin:  ")
    else:
        print ("Please enter a valid command")
        start = input("Type start or tutorial to begin:  ")

player = curr_player
checkmate = False
valid = False
current_value = input("Player " + curr_player + " " + "please enter co-ordinates in the form RowColumn.  ")

#turn taking and gameplay

while checkmate == False:
    while valid == False:
        while validcheck_start()==False:
            #validity check for inputs
            current_value = input("Your input is invalid. Please try again.  ")

        current_value = list(map(int, current_value))

        end = input(curr_player + " " + "please enter co-ordinates you want to move the piece to.  ")

        while validcheck_end()==False:
            end = input("Your input is invalid. Please try again.  ")

        end = list(map(int, end))
        #validity check for pieces
        valid = piece_move_match(Startboard, current_value[0], current_value[1], end[0], end[1])
        if valid == False:
            current_value = input("Your piece is invalid. Please enter the coordinates of the piece you want to move again.  ")
    move(Startboard, current_value[0], current_value[1], end[0], end[1])

    indexed_board(Startboard)

    curr_player = opp(curr_player)

    if is_check(Startboard, curr_player):
        checkmate = is_checkmate(Startboard, curr_player)
        #resets the variables for the next turn
    valid  = False
    current_value = input(curr_player + " " + "please enter co-ordinates.  ")

#Message at the end of the game
print ("Checkmate! Player " + str(opp(curr_player)) + " wins!")



