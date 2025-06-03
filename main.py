#chess pieces
#LATER vacant_w = "o"
#LATER vacant_b = "0"
vacant = "o"
#White
white_king = "♔"
white_queen = "♕"
white_rook = "♖"
white_bishop = "♗"
white_knight = "♘"
white_pawn = "♙"
white_pieces = [white_king,white_queen,white_rook,white_bishop,white_knight,white_pawn]
#Black
black_king = "♚"
black_queen = "♛"
black_rook = "♜"
black_bishop = "♝"
black_knight = "♞"
black_pawn = "♟"
black_pieces = [black_king,black_queen,black_rook,black_bishop,black_knight,black_pawn]
#Pieces
pawn = white_pawn or black_pawn
knight = white_knight or black_knight
bishop = white_bishop or black_bishop
rook = white_rook or black_bishop
queen = white_queen or black_queen
king = white_king or black_king


############################################################
#COMMAND
#
#Player_move -> Legal Move checker -> U know what I am a turtle
#
#
#
#
#
#


#BOARD
############################################################
"""
  0 1 2 3 4 5 6 7
0 A               [0] E.g. This is whites king starting row
1   B
2
3
4
5
6
7                 [7] E.g. Blacks Kings Starting Row


A = [0][0]
B = [1][1]


"""
############################################################
### Row 1, Row 2, Row 3, Row 4, Row 5, Row 6, Row 7, Row 8
board = [["0 ","1","2","3","4","5","6","7","8"],["1 ",white_rook,white_knight,white_bishop,white_queen,white_king,white_bishop,white_knight,white_rook],["2 ",white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn],["3 ",vacant,vacant,vacant,vacant,vacant,vacant,vacant,vacant,],["4 ",vacant,vacant,vacant,vacant,vacant,vacant,vacant,vacant,],["5 ",vacant,vacant,vacant,vacant,vacant,vacant,vacant,vacant,],["6 ",vacant,vacant,vacant,vacant,vacant,vacant,vacant,vacant,],["7 ",black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,],["8 ",black_rook,black_knight,black_bishop,black_queen,black_king,black_bishop,black_knight,black_rook]]




#Displays the Board
def print_board():
    for i in range(8,-1,-1):
        print("".join(board[i]))
#Changes the Board
def board_change():
    board[finishing_square_y][finishing_square_x] = board[starting_square_y][starting_square_x]  
    board[starting_square_y][starting_square_x] = vacant
    print_board()
   




############################################################
#Movement -> legal Move? -> #Checks --> On a Peasant
def player_move():
    global starting_square_x, starting_square_y, finishing_square_x, finishing_square_y
    #Starting Square
    starting_square_x = int(input("Enter x axis coordinate of the square which you piece is on: "))
    starting_square_y = int(input("Enter y axis coordinate of the square which you piece is on: "))
    #Prints Piece and location
    print(f"Your {board[starting_square_y][starting_square_x]} is ({starting_square_x},{starting_square_y})")
    #Ending Square
    finishing_square_x = int(input("Enter x axis coordinate of the square which you piece is going to go: "))
    finishing_square_y = int(input("Enter y axis coordinate of the square which you piece is going to go: "))
    print(f"Your pieces finishing Square is ({finishing_square_x},{finishing_square_y})")


   




   


    #TRANSITION TO LEGAL MOVE CHECKER
    legal_move_checker()
    if end_game == False:
        player_move()


#LEGAL Move CHECKERS
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################


def pentration_through_pieces_checker_horizontal(): # X axis
    pentration = False
    direction = "neutral"
    distance_start_finish_x = finishing_square_x - starting_square_x
    # Checks the directions , Right and Left
    if distance_start_finish_x < 0:
       direction = "left"
    if distance_start_finish_x > 0:
       direction = "right"


    if direction == "left":
       for i in range(distance_start_finish_x): # Counts up from 0 1 2 3
           #TESTING
           #print("test 2")
           #print(board[starting_square_y + 1 + i][starting_square_x])  #!!! DONT DO THIS WHY ADD On the the x axis
         
           #print(starting_square_y + 1 + i)
           if board[starting_square_x + i + 1][starting_square_y]  != vacant: # Without i variable being added the variable starting squrare wouldn't change
               pentration = True # WHAT THE FLIPPING DODOLES   #Somehow o = o makes it else NEED HELP!!! NEvermind # I think i fiqured it out. + 1 is needed so it doesn't check the square which its on
               print("That illegal you tried to pentetrate a piece only the knight can do that")
               break
           else:
               print("Penetration test Passed")


    if direction == "right":
       
       for i in range(distance_start_finish_x*-1): # times minus 1 Turns the negative into a positve
           if board[starting_square_x - i - 1][starting_square_y] != vacant: # Negative Hmmm
               pentration = True
               print("That illegal you tried to pentetrate a piece only the knight can do that (2)")
               break
           else:
               print("Penetration test Passed")
    #PARAMETER PASSING 
    return pentration




def pentration_through_pieces_checker_verticle(): # Y axis
   direction = "neutral"
   pentration = False
   distance_start_finish_y = finishing_square_y - starting_square_y
   


   #CHECKS UP DOWN
   #Negative checks Downards
   
   if distance_start_finish_y < 0:
       direction = "down"
    #Postive Checks Upwards
   if distance_start_finish_y > 0:
       direction = "up"


   #CHECKS If theres something in between the start and destination
   if direction == "up":
       for i in range(distance_start_finish_y): # Counts up from 0 1 2 3
           #TESTING
           #print("test 2")
           #print(board[starting_square_y + 1 + i][starting_square_x])  #!!! DONT DO THIS WHY ADD On the the x axis
         
           #print(starting_square_y + 1 + i)
           if board[starting_square_y + i + 1][starting_square_x]  != vacant: # Without i variable being added the variable starting squrare wouldn't change
               pentration = True # WHAT THE FLIPPING DODOLES   #Somehow o = o makes it else NEED HELP!!! NEvermind # I think i fiqured it out. + 1 is needed so it doesn't check the square which its on
               print("That illegal you tried to pentetrate a piece only the knight can do that")
               break
           else:
               print("Penetration test Passed")
               
               
           
   if direction == "down":
       for i in range(distance_start_finish_y*-1): #Turns the negative into a positve
           print("test 4")
           if board[starting_square_y - i - 1][starting_square_x] != vacant: # Negative Hmmm
               pentration = True
               print("That illegal you tried to pentetrate a piece only the knight can do that (2)")
               break
           else:
               print("Penetration test Passed")
   return pentration
               
           


def legal_move_enforcer():
    #Prints If Illegal Move has been played
    if legal_move == True:
        print("That was a illegal move Please play again")
        player_move() #LOOP OF Henle
    #Carries on the code and prints the board
    elif legal_move == False:
        print("Valid Move :)")
        board_change()


def legal_move_checker():
    global legal_move
    #Legal Move Checker
    legal_move = False
    #PAWN
#pawn normal move
    #checks if pawn moves
    if pawn == board[starting_square_y][starting_square_x]: #board[starting_square_y][starting_square_x] = The piece which is moved
        pentration_through_pieces_checker_verticle()
        #IF STATEMENT FOR IF IT NOT ON STARTING SQUARE
        if starting_square_y != 2:
    #checks if pawn moves one square forward Illegal Move Checker
                if starting_square_x != finishing_square_x:
                    if board[starting_square_y + 1][starting_square_x + 1] == vacant and board[starting_square_y + 1][starting_square_x -1 ] == vacant:
                        print("That piece cant take like that(4)")
                        legal_move = True
                else:
                    if starting_square_y + 1 != finishing_square_y: #or starting_square_x != finishing_square_x:
                        print("That piece cant move like that (1)")
                        legal_move = True
    #pawn charge Illegal Move Checker
        else:
    #pawn takes Illegal Move Checker
                if starting_square_x != finishing_square_x:
                    if board[starting_square_y + 1][starting_square_x + 1] == vacant and board[starting_square_y + 1][starting_square_x -1 ] == vacant:
                        print("That piece cant take like that(4)")
                        legal_move = True
                else:
                    if starting_square_y + 1 != finishing_square_y and starting_square_y + 2 != finishing_square_y: #or starting_square_x != finishing_square_x: # for some reason And acts like or idk
                        print("That piece cant move like that (3)")
                        legal_move = True
    #on peasant
    #KNIGHT
     
    #BISHOP
    #ROOK
    #QUEEN
    #KING
    if king == board[starting_square_y][starting_square_x]:
        pentration = pentration_through_pieces_checker_verticle()
        pentration  = pentration_through_pieces_checker_horizontal()
        if pentration == True: #Checks if the moves goes through any pieces
            legal_move = True #TURNS LEGAL MOVES TO TRUE
            #DONT USE LEGAL_MOVE == TRUE
            legal_move_enforcer()


           
   
    #print(legal_move) Some how legal_move turnss false
    legal_move_enforcer()
#Players


def name_choose():
    global player_1_name , player_2_name
    player_1_name = input("Choose Your Name Player One!")
    player_2_name = input("Choose Your Name Player Two!")








#Win Lose Draw
end_game = False
#optional
#Time
#########################################################################################################
###########OOOOOOO###OOOOOOO#############################################################################
##############/O######O/#################################################################################
##############//######//#################################################################################
#########################################################################################################
#########################################################################################################
# STEEL BALL RUN
print_board()
player_move()







