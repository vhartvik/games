from hangman import Hangman
from tictactoe import TicTacToe

def main():
    while True:
        game = input("Please select a game to play:\n"
            "Type H to play Hangman\n"
            "Type T to play Tic Tac Toe\n"
            "Type Q to quit\n")
        if game == "H":
            new_game = Hangman("Hangman", "Will you escape the noose?")
            new_game.play_game()
        elif game == "T":
            new_game = TicTacToe("Tic Tac Toe", "Can you outsmart me?")
            new_game.play_game()
        elif game == "Q":
            print("Goodbye :'(")
            quit()
        else:
            print("Sorry, that was not a valid selection.")


if __name__ == '__main__':
    main()
