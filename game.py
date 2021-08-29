class Game:
    def __init__(self, name, game_intro):
        self.name = name
        self.game_intro = game_intro

    def play_game(self):
        """Prints the game intro"""
        print(f"\nIt's time to play {self.name}!\n{self.game_intro}\n")

    def play_again(self, parting_remark):
        """Asks player if they want to play again, and if so restarts game"""
        play_again = input(f"{parting_remark}"
            "Would you like to try again? Y/N ")
        if play_again == "Y":
            print("Here we go again!")
            self.play_game()
        else:
            print("Sorry to see you go! Have a great day!")

    def player_wins(self):
        """Congradulates the player on winning"""
        self.play_again(f"Congradulations you won {self.name}!\n\n")

    def player_loses(self):
        """Wishes the player better luck next time"""
        self.play_again(f"Better luck next time playing {self.name}.\n\n")
