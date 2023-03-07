# group number: 23
# student names: Eric Zhou, Amaan Siddiqi, Thomas Wood, Daniel Ding

import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """

        print(self.board[0]+"   |   " + self.board[1] + "   |   " + self.board[2] + "     " + "0" + "   |   " + "1" + "   |   " + "2")
        print("- - + - - - + - -     - - + - - - + - -")

        print(self.board[3]+"   |   " + self.board[4] + "   |   " + self.board[5] + "     " + "3" + "   |   " + "4" + "   |   " + "5")
        print("- - + - - - + - -     - - + - - - + - -")

        print(self.board[6]+"   |   " + self.board[7] + "   |   " + self.board[8] + "     " + "6" + "   |   " + "7" + "   |   " + "8")

        return #To Implement

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        player = "X"
        userInput = input("Next move for X (state a valid cell num): ")
        if not userInput.isdigit() or int(userInput) > 8 or int(userInput) < 0:
            print("Must enter a valid cell number")
            self.playerNextMove()
        elif int(userInput) in self.played:
            print("Cell already played")
            self.playerNextMove()
        else:
            cellNum = int(userInput)
            print(f"You chose cell {cellNum}")
            print(self.played)
            self.board[cellNum] = player
            self.played.add(cellNum)
            self.printBoard()
        return #To Implement

    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        cellNum = random.choice([x for x in range(9) if x not in self.played])
        self.board[cellNum] = "O"
        self.played.add(cellNum)
        print(f"Computer chose cell {cellNum}")
        print(self.played)
        self.printBoard()
        return #To Implement

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        wins = ([0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8], 
            [2, 4, 6])

        player = set()

        for i, v in enumerate(self.board):
            if v == who:
                player.add(i)

        for w in wins:
            if set(w).issubset(player):
                return True

        return False #To Implement

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        if self.hasWon("X"):
            print("You won! Thanks for playing.")
            return True
        elif len(self.played) == 9:
            print("A draw! Thanks for playing.")
            return True
        elif self.hasWon("O"):
            print("You lost! Thanks for playing")
            return True
        return False #To Implement

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate