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
#All Pieces
all_pieces = [white_king,white_queen,white_rook,white_bishop,white_knight,white_pawn,black_king,black_queen,black_rook,black_bishop,black_knight,black_pawn]

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

def pentration_through_pieces_checker_diagnol(): #AHHHHHH
    pentration = False
    direction = "neutral"
    distance_start_finish_x = finishing_square_x - starting_square_x
    distance_start_finish_y = finishing_square_y - starting_square_y 

    # DOWN 
    if distance_start_finish_y < 0:
        if distance_start_finish_x < 0: 
            direction = "down_left" 
            print("t1")
        elif distance_start_finish_x > 0:
            direction = "down_right"
            print("t2")
    
    #UP
    elif distance_start_finish_y > 0:
        if distance_start_finish_x < 0: #
            direction = "up_left"
            print("t3")
        elif distance_start_finish_x > 0:
            direction = "up_right"
            print("t4")


    #CONVERTS EACH 
    if distance_start_finish_x < 0:
           positive_distance_start_finish_x = distance_start_finish_x * -1
           print("JRBRB")
    if distance_start_finish_y < 0:   
           positive_distance_start_finish_y = distance_start_finish_y * -1
           print("OEE")

    #This is need due to the variable positive_distance_start_finish_x needing to be ASSIGNED to something
    if distance_start_finish_x > 0: 
           positive_distance_start_finish_x = distance_start_finish_x
           print("HEHR")
    if distance_start_finish_y > 0:
           positive_distance_start_finish_y = distance_start_finish_y
           print("London Turtles Furtling A Burtle")
           

   
    positive_distance_start_finish_xy = positive_distance_start_finish_y + positive_distance_start_finish_x


    # DOWN LEFT

    if direction == "down_left": 
       print("t222")
       for i in range(positive_distance_start_finish_xy): # Counts up from 0 
           print(board[starting_square_y - i - 1][starting_square_x - i - 1])
           if board[starting_square_y - i - 1][starting_square_x - i - 1]  != vacant: # You dont swithc the variation of board[][] but the difference between the two penetrations is that the + i + 1 is on the other 
               pentration = True # WHAT THE FLIPPING DODOLES   #Somehow o = o makes it else NEED HELP!!! NEvermind # I think i fiqured it out. + 1 is needed so it doesn't check the square which its on
               print("That illegal you tried to pentetrate a piece only the knight can do that (9034)")
               break
           else:
               print("Penetration test Passed")

    # DOWN RIGHT

    if direction == "down_right":
       print("t424")
       for i in range(positive_distance_start_finish_xy): # Counts up from 0 
           print(board[starting_square_y - i - 1][starting_square_x + i + 1])
           if board[starting_square_y - i - 1][starting_square_x + i + 1]  != vacant: # You dont swithc the variation of board[][] but the difference between the two penetrations is that the + i + 1 is on the other 
               pentration = True # WHAT THE FLIPPING DODOLES   #Somehow o = o makes it else NEED HELP!!! NEvermind # I think i fiqured it out. + 1 is needed so it doesn't check the square which its on
               print("That illegal you tried to pentetrate a piece only the knight can do that (9084)")
               break
           else:
               print("Penetration test Passed")

    #UP LEFT

    if direction == "up_left":
        print("t431")
        print(positive_distance_start_finish_xy)
        for i in range(positive_distance_start_finish_xy): # Counts up from 0 
           print(board[starting_square_y + i + 1][starting_square_x - i - 1])
           if board[starting_square_y + i + 1][starting_square_x - i - 1]  != vacant: 
               pentration = True
               print("That illegal you tried to pentetrate a piece only the knight can do that (9073)")
               break
           else:
               print("Penetration test Passed")
        
    #UP RIGHT

    if direction == "up_right":
        print("t241")
        for i in range(positive_distance_start_finish_xy): # Counts up from 0 
           print(board[starting_square_y + i + 1][starting_square_x + i + 1])
           if board[starting_square_y + i + 1][starting_square_x + i + 1]  != vacant: 
               pentration = True
               print("That illegal you tried to pentetrate a piece only the knight can do that (9033)")
               break
           else:
               print("Penetration test Passed")
        
    return pentration


    


def pentration_through_pieces_checker_horizontal(): # X axis
    pentration = False
    direction = "neutral"
    distance_start_finish_x = finishing_square_x - starting_square_x                                # ON THIS LINE it 
    # Checks the directions , Right and Left 
    if distance_start_finish_x > 0:
       direction = "left"                               # AYAHAHAH LOOK HERE DONT CHANGE THE RIGHT LEFT.  ^^^^ 
    if distance_start_finish_x < 0:
       direction = "right"

    print(direction)#test

    if direction == "left":
       for i in range(distance_start_finish_x): # Counts up from 0 1 2 3
           #TESTING
           #print("test 2") 
           #print(board[starting_square_y + 1 + i][starting_square_x])  #!!! DONT DO THIS WHY ADD On the the x axis
          
           #print(starting_square_y + 1 + i)

           if board[starting_square_y][starting_square_x + i + 1]  != vacant: # You dont swithc the variation of board[][] but the difference between the two penetrations is that the + i + 1 is on the other 
               pentration = True # WHAT THE FLIPPING DODOLES   #Somehow o = o makes it else NEED HELP!!! NEvermind # I think i fiqured it out. + 1 is needed so it doesn't check the square which its on
               print("That illegal you tried to pentetrate a piece only the knight can do that (9283)")
               break
           else:
               print("Penetration test Passed")

    if direction == "right":
       

       
       for i in range(distance_start_finish_x*-1): # times minus 1 Turns the negative into a positve

           if board[starting_square_y][starting_square_x - i - 1] != vacant: # Negative Hmmm
               pentration = True
               print("That illegal you tried to pentetrate a piece only the knight can do that (2)")
               break
           else:
               print("Penetration test Passed")
               
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
               print("That illegal you tried to pentetrate a piece only the knight can do that (0183)")
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
        print_board()
        print("Illegal Eagle Feeble Tyranorsoup ")
        player_move() #LOOP OF Henle
    #Carries on the code and prints the board
    elif legal_move == False:
        print("Valid Move :)")
        board_change()

def legal_move_checker():
    global legal_move 
    #Legal Move Checker
    legal_move = False
    #Prevents the use of pieces which are not pieces.  e.g vacant square
    if all_pieces != board[starting_square_y][starting_square_x]:
        print("Hey \nHey \nHey \n Thats not you piece to move ")
        legal_move = True
    #PAWN 
#pawn normal move 
    #checks if pawn moves 
    #DO A SEPERATE ONE FOR BLACK PAWN
    if white_pawn == board[starting_square_y][starting_square_x]: #board[starting_square_y][starting_square_x] = The piece which is moved
        pentration_through_pieces_checker_verticle()
        #IF STATEMENT FOR IF IT NOT ON STARTING SQUARE
        if starting_square_y != 2:
        #checks if pawn moves one square forward Illegal Move Checker
                if starting_square_x != finishing_square_x:
                    if board[starting_square_y + 1][starting_square_x + 1] == vacant and board[starting_square_y + 1][starting_square_x -1 ] == vacant:
                        print("That piece cant take like that(4783)")
                        legal_move = True
                else:
                    if starting_square_y + 1 != finishing_square_y: #or starting_square_x != finishing_square_x:
                        print("That piece cant move like that (1643)")
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
                        print("That piece cant move like that (3543)")
                        legal_move = True
        #BLACK PAWN
    if black_pawn == board[starting_square_y][starting_square_x]: #board[starting_square_y][starting_square_x] = The piece which is moved
        pentration_through_pieces_checker_verticle()
        #IF STATEMENT FOR IF IT NOT ON STARTING SQUARE
        if starting_square_y != 2:
        #checks if pawn moves one square forward Illegal Move Checker
                if starting_square_x != finishing_square_x:
                    if board[starting_square_y + 1][starting_square_x + 1] == vacant and board[starting_square_y + 1][starting_square_x -1 ] == vacant:
                        print("That piece cant take like that(4345)")
                        legal_move = True
                else:
                    if starting_square_y + 1 != finishing_square_y: #or starting_square_x != finishing_square_x:
                        print("That piece cant move like that (1213)")
                        legal_move = True
        #pawn charge Illegal Move Checker
        else:
        #pawn takes Illegal Move Checker
                if starting_square_x != finishing_square_x:
                    if board[starting_square_y + 1][starting_square_x + 1] == vacant and board[starting_square_y + 1][starting_square_x -1 ] == vacant:
                        print("That piece cant take like that(4452)")
                        legal_move = True
                else:
                    if starting_square_y + 1 != finishing_square_y and starting_square_y + 2 != finishing_square_y: #or starting_square_x != finishing_square_x: # for some reason And acts like or idk 
                        print("That piece cant move like that (3124)")
                        legal_move = True
        #on peasant 

    #KNIGHT
    if knight == board[starting_square_y][starting_square_x]:
        #knight Moves
            #Checks if the knight does not move in L shape .   STRUCT = Up . Side

            #Old COde  not ((((starting_square_x + 1) or (starting_square_x - 1)) == finishing_square_x and ((starting_square_y + 3) or (starting_square_y - 3)) == finishing_square_y) or (((starting_square_y + 1) or (starting_square_y - 1)) == finishing_square_y and ((starting_square_x + 3) or (starting_square_x -3)) == finishing_square_x)): 
        
        if not ((starting_square_x + 1 == finishing_square_x) or (starting_square_x - 1 == finishing_square_x ))  or (((starting_square_y + 1 == finishing_square_y) or (starting_square_y - 1 == finishing_square_y))):  
                # Nested if statement.  First checks for a if the knight moves by one in any direction.
                if not (((starting_square_y + 3 == finishing_square_y ) or (starting_square_y - 3 == finishing_square_y)) or ((starting_square_x + 3 == finishing_square_x) or (starting_square_x -3 == finishing_square_x))):
                    #The second checks for a three extension in any direction.
                    print("Your Horsey Cant Move like that (8341)")
                    legal_move = True
            
            

        # HORse CAN JUMP OVER PIECES

    #BISHOP
    if bishop == board[starting_square_y][starting_square_x]:
        #bishop moves
        if not(starting_square_x > finishing_square_x and starting_square_y > finishing_square_y or starting_square_x > finishing_square_x  and starting_square_y < finishing_square_y or starting_square_x < finishing_square_x  and starting_square_y > finishing_square_y or starting_square_x < finishing_square_x  and starting_square_y < finishing_square_y ): 
            # checks for diagnols . Copied from Rook
            print("Your Piece Can not move like that 2489")
            legal_move = True 
        pentration_b1 = pentration_through_pieces_checker_diagnol()
        if pentration_b1:
            legal_move = True

    #ROOK
    if rook == board[starting_square_y][starting_square_x]:
        #Rook Moves 
         if (starting_square_x > finishing_square_x and starting_square_y > finishing_square_y or starting_square_x > finishing_square_x  and starting_square_y < finishing_square_y or starting_square_x < finishing_square_x  and starting_square_y > finishing_square_y or starting_square_x < finishing_square_x  and starting_square_y < finishing_square_y ) or (): 
            #Checks if the rook moves diagonolly
            print("Your Piece Can not move like that 2484")
            legal_move = True 
        
         pentration_r1 = pentration_through_pieces_checker_verticle()
    
         if pentration_r1 == True: 
            legal_move = True
         
        
    #QUEEN
    if queen == board[starting_square_y][starting_square_x]:
        #Queen Moves

        #Checks if the queen does not move diagonolly or horisontally or vertically 
        if not((starting_square_x > finishing_square_x and starting_square_y > finishing_square_y or starting_square_x > finishing_square_x  and starting_square_y < finishing_square_y or starting_square_x < finishing_square_x  and starting_square_y > finishing_square_y or starting_square_x < finishing_square_x  and starting_square_y < finishing_square_y) or (starting_square_x > finishing_square_x and starting_square_y == finishing_square_y or starting_square_x < finishing_square_x and starting_square_y == finishing_square_y) or (starting_square_y > finishing_square_y and starting_square_x == finishing_square_x or starting_square_y < finishing_square_y and starting_square_x == finishing_square_x)):
                legal_move = True
                print("Your Piece Can not move like that 2431")
        
        #Original didn't work due to having a "not" in each check. e.g. not diagonol , not horisontal etc.  Putting not in one place justs makes it work. 
            
        
            

        #COPIED FROM KING
        if True: 
            if not(starting_square_x > finishing_square_x or starting_square_x < finishing_square_x and starting_square_y > finishing_square_y or starting_square_y < finishing_square_y): 
                # Checks if the piece is not going diagonally. < to see any length of diagnol movement

                pentration_q1  = pentration_through_pieces_checker_horizontal() # two different variables to make it so the second penetration check doesn't mess with the first one
                pentration_q2 = pentration_through_pieces_checker_verticle() 

                if pentration_q1 or pentration_q2 == True: #Needs to be here to prevent Unbound local error    
                    legal_move = True   
            else:
                pentration_q3 = pentration_through_pieces_checker_diagnol() 
                if pentration_q3 == True: #Needs to be here to prevent Unbound local error
                    legal_move = True #TURNS LEGAL MOVES TO TRUE 
        

    #KING
    if king == board[starting_square_y][starting_square_x]:
        #King Moves 
        if (starting_square_y + starting_square_x) + 1 != (finishing_square_y + finishing_square_x): # Checks the if the movement is NOT to the (FRONT BACK LEFT OR RIGHT) of the piece
            if not(starting_square_x + 1 == finishing_square_x  and starting_square_y + 1 == finishing_square_y or starting_square_x - 1 == finishing_square_x  and starting_square_y - 1 == finishing_square_y or starting_square_x - 1 == finishing_square_x  and starting_square_y + 1 == finishing_square_y or starting_square_x + 1 == finishing_square_x  and starting_square_y - 1 == finishing_square_y ): 
            #Checks if the squares are NOT to the DIAGNOLS of the piece. Both + and minus to check both sides 
                legal_move = True
                print("Your Piece Can not move like that 2421")
        #RIGHT OR LEFT CHECKER.
        if True: 
            if not(starting_square_x > finishing_square_x or starting_square_x < finishing_square_x and starting_square_y > finishing_square_y or starting_square_y < finishing_square_y): 
                # Checks if the piece is not going diagonally. Bigger than to see any length of diagnol movement

                pentration_k1  = pentration_through_pieces_checker_horizontal() # two different variables to make it so the second penetration check doesn't mess with the first one
                pentration_k2 = pentration_through_pieces_checker_verticle() 

                if pentration_k1 or pentration_k2 == True: #Needs to be here to prevent Unbound local error    
                    legal_move = True   
            else:
                pentration_k3 = pentration_through_pieces_checker_diagnol() 
                if pentration_k3 == True: #Needs to be here to prevent Unbound local error
                    legal_move = True #TURNS LEGAL MOVES TO TRUE     
        #CASTLING


    

            
   
    #print(legal_move) Some how legal_move turnss false
    legal_move_enforcer()
#Players

def name_choose():
    player_1_name = input("Choose Your Name Player One!")
    player_2_name = input("Choose Your Name Player Two!")
    return player_1_name , player_2_name




#Win Lose Draw
end_game = False 
#optional
#Time
#########################################################################################################
###########OOOOOOO###OOOOOOO#############################################################################
# STEEL BALL RUN
print_board()
player_move()


