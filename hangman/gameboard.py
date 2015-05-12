__author__ = 'Alexis'

class GameBoard(object):

    def __init__(self, words):
        self.board = []
        self.words = words
        self.guess_wrong = 0
        self.guess_right = 0

    def setupBoard(self):
        self.board.append([" "] * 2 + ["+"] + ["-"] * 6 + ["+"])
        self.board.append([" "] * 2 + ["|"] + [" "] * 6 + ["|"])
        for x in range(7):
            self.board.append([" "] * 9 + ["|"])
        self.board.append([" "] * 2 + ["="] * 7 + ["+"])
        for x in range(1):
             self.board.append([" "] * 9)
        line_letters = []
        for letter in self.words:
            if letter == " ":
                line_letters.append(letter)
            else:
                line_letters.append("_")
        self.board.append(line_letters)
        self.board.append([" "] * 9)



    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def getGuess(self, guess):
        indices = self.find(self.words, guess)
        underscore = self.board[-4]
        for index in indices:
            underscore[index] = guess
        self.board[-4] = underscore


    def guessWrong(self, guess):
        if guess not in self.words:
            self.guess_wrong += 1
            if self.guess_wrong == 1:
                self.board[2][2] = "0"
            if self.guess_wrong == 2:
                self.board[3][2] = "|"
            if self.guess_wrong == 3:
                self.board[3][1] = "/"
            if self.guess_wrong == 4:
                self.board[3][3] = "\\"
            if self.guess_wrong == 5:
                self.board[4][1] = "/"
            if self.guess_wrong == 6:
                self.board[4][3] = "\\"
            elif self.guess_wrong > 6:
                return "You lost the game!"
        if guess in self.words:
           self.guess_right += 1

    def printBoard(self):
        for row in self.board:
            print " ".join(row)




