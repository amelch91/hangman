__author__ = 'Alexis'

import getpass
import sys
from gameboard import GameBoard
from thegame import TheGame

if __name__ == '__main__':
    while True:
        words = getpass.getpass(prompt='Please enter words: ')
        words = words.lower()
        gameboard = GameBoard(words)
        gameboard.setupBoard()
        gameboard.board.append(["Letters guessed:"])
        letters_guessed = []
        gameboard.board.append(letters_guessed)
        while gameboard.guess_wrong < 6:
            guess = raw_input("What is your guess?")
            guess = guess.lower()
            letters_guessed.append(guess)
            gameboard.getGuess(guess)
            gameboard.guessWrong(guess)
            gameboard.printBoard()
            if gameboard.guess_right == len(words):
                print "You win!"
                play_again = raw_input("Would you like to play again? (Y/N)")
                if play_again == "Y":
                    break
                else:
                    print "Thanks for playing!"
                    sys.exit(0)
        if gameboard.guess_wrong >= 6:
            print "You lose! The word was %s." % words
            play_again = raw_input("Would you like to play again? (Y/N)")
            if play_again == "Y":
                continue
            else:
                print "Thanks for playing!"
                sys.exit(0)









