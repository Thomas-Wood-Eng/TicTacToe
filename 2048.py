# group number: 23
# student names: Eric Zhou, Amaan Siddiqi, Thomas Wood, Daniel Ding
import random, sys

class TwentyFortyEight:
    def __init__(self) -> None: # Use as is
        """ 
            initializes the board data field
            and displays the initial board
            and prints a welcome message
        """

        self.board: list = []  # a 2-D list to keep current status of the game board
        for _ in range(4):     # initialize the board cells/tiles with ''
            rowList = []
            for _ in range(4):
                rowList.append('')
            self.board.append(rowList)

        # add two starting 2's at random cells; using a trivial search
        countOfTwosPlacedAtTheBeginning = 0  
        while countOfTwosPlacedAtTheBeginning < 2:  
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if self.board[row][column] == '': # if not already taken
                self.board[row][column] = 2
                countOfTwosPlacedAtTheBeginning += 1
        
        print(); print("Welcome! Let's play the 2048 game."); print()
    

    def displayGame(self) -> None:  # Use as is
        """ displays the current board on the console """

        print("+-----+-----+-----+-----+")
        for row in range(4): 
            for column in range(4):
                cell = self.board[row][column] 
                print(f"|{str(cell).center(5)}", end="")
            print("|")
            print("+-----+-----+-----+-----+")


    def addANewTwoToBoard(self) -> None:

        """ 
            Adds a 2 to a random tile in the game
            Ensures that the tile is empty before adding
        """
        
        validBox = False

        while(not validBox):
            row = random.randint(0, 3)
            collumn = random.randint(0, 3)

            if self.board[row][collumn] == '':
                validBox = True
        
        self.board[row][collumn] = 2


    def isFull(self) -> bool:

        """ 
            Checks whether the board is full
            True if full (ends the game) else false
        """

        for row in range(4):
            for collumn in range(4):
                if self.board[row][collumn] == '':
                    return False

        return True 


    def getCurrentScore(self) -> int:
        """ 
            calculates and returns the score
            the score is the sum of all the numbers currently on the board
        """
        score = 0
        for i in range(4):
            for j in range(4):
                if(self.board[i][j] != ''):
                    score += self.board[i][j]

        return score

    def updateTheBoardBasedOnTheUserMove(self, move: str) -> None:
        """
            updates the board field based on the move argument
            the move argument is either 'W', 'A', 'S', or 'D'
            directions: W for up; A for left; S for down, and D for right
        """

        if(move == 'A'):
            #for tries in range(4):
            for i in range(4):
                for j in range(4):
                    if(j==0):
                        continue
                    if(self.board[i][j]==''):
                        continue
                    k = j
                    while(self.board[i][k-1]=='' and k>=1):
                        self.board[i][k-1] = self.board[i][k]
                        self.board[i][k] = ''
                        k = k-1
                    if(self.board[i][k-1] == self.board[i][k]):
                        self.board[i][k-1] = str(self.board[i][k-1]+self.board[i][k])
                        self.board[i][k] = ''
            
            for i in range(4):
                for j in range(4):
                    if(self.board[i][j]==''):
                        continue
                    if(str(self.board[i][j])):
                        self.board[i][j] = int(self.board[i][j])
            #game.displayGame()
            
        if(move == 'W'):
            #for tries in range(4):
            for i in range(4):
                for j in range(4):
                    if(i==0):
                        continue
                    if(self.board[i][j]==''):
                        continue
                    k = i
                    while(self.board[k-1][j]=='' and k>=1):
                        self.board[k-1][j] = self.board[k][j]
                        self.board[k][j] = ''
                        k = k - 1
                    if(self.board[k-1][j] == self.board[k][j]):
                        self.board[k-1][j] = str(self.board[k-1][j]+self.board[k][j])
                        self.board[k][j] = ''
            
            for i in range(4):
                for j in range(4):
                    if(self.board[i][j]==''):
                        continue
                    if(str(self.board[i][j])):
                        self.board[i][j] = int(self.board[i][j])

        if(move == 'S'):
            for tries in range(4):
                for i in range(4):
                    for j in range(4):
                        if(i==3):
                            continue
                        if(self.board[i][j]==''):
                            continue
                        k = i
                        while(self.board[k+1][j]=='' and k<=3):
                            self.board[k+1][j] = self.board[k][j]
                            self.board[k][j] = ''
                            "k = k + 1"
                        if(self.board[k+1][j] == self.board[k][j]):
                            self.board[k+1][j] = str(self.board[k+1][j]+self.board[k][j])
                            self.board[k][j] = ''
            
            for i in range(4):
                for j in range(4):
                    if(self.board[i][j]==''):
                        continue
                    if(str(self.board[i][j])):
                        self.board[i][j] = int(self.board[i][j])
            #game.displayGame()
            
        if(move == 'D'):
            for tries in range(4):
                for i in range(4):
                    for j in range(4):
                        if(j==3):
                            continue
                        if(self.board[i][j]==''):
                            continue
                        k = j
                        while(self.board[i][k+1]=='' and k<3):
                            self.board[i][k+1] = self.board[i][k]
                            self.board[i][k] = ''
                        if(self.board[i][k+1] == self.board[i][k]):
                            self.board[i][k+1] = str(self.board[i][k+1]+self.board[i][k])
                            self.board[i][k] = ''
            
            for i in range(4):
                for j in range(4):
                    if(self.board[i][j]==''):
                        continue
                    if(str(self.board[i][j])):
                        self.board[i][j] = int(self.board[i][j])
            #game.displayGame()
            
                        
        return None


if __name__ == "__main__":  # Use as is
    def promptGamerForTheNextMove() -> str: #A function used in super-loop
        """
            prompts the gamer to select the next move or Q (to quit)
            valid move direction: one of 'W', 'A', 'S' or 'D'.
            either returns a valid move direction or terminates the game
        """
        print("Enter one of WASD (move direction) or Q (to quit)")
        while True:  # prompt until a valid input is entered
            move = input('> ').upper()
            if move in ('W', 'A', 'S', 'D'): # a valid move direction
                return move  
            if move == 'Q': # for quit
                print("Exiting the game. Thanks for playing!")
                sys.exit()
            print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
   
    game = TwentyFortyEight()

    while True:  # Super-loop for the game
        game.displayGame()
        print(f"Score: {game.getCurrentScore()}")
        game.updateTheBoardBasedOnTheUserMove(promptGamerForTheNextMove())
        game.addANewTwoToBoard()

        if game.isFull():
            game.displayGame()
            print("Game is over. Check out your score.")
            print("Thanks for playing!")
            break