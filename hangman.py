from random import randint

from categories import animal_words, harry_potter_words, vegetable_words, winter_words
from game import Game

class Hangman(Game):
    EASY = "E"
    MEDIUM = "M"
    HARD = "H"
    EASY_LIVES = 12
    MEDIUM_LIVES = 6
    HARD_LIVES = 3
    CATEGORY_ANIMALS = "A"
    CATEGORY_HP = "H"
    CATEGORY_VEGETABLES = "V"
    CATEGORY_WINTER = "W"

    def __init__(self, name, game_intro):
        super().__init__(name, game_intro)
        self.letters_guessed = []
        self.hidden_word = ""
        self.guessed_word = ""
        self.num_wrong_guesses = 0
        self.turn = 0
        self.lives = 0
        self.right_character_count = 0
        self.category = ""

    def print_hangman(self):
        """Prints out visual representation of the hangman state.
        
        Returns: None
        """
        HANGMAN_STAGES = ['''
     |----------|
     |
     |
     |
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |  
     |
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |          |
     |
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|
     |
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|
     |        /
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        /
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        /   \\
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        / | \\
     |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        / | \\
     |          |
     |
     |
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        / | \\
     |          |
     |         /
     |        /
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        / | \\
     |          |
     |         /
     |       _/
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        / | \\
     |          |
     |         / \\
     |       _/   \\
     |
  ___|___''', '''
     |----------|
     |         ( )
     |         _|_
     |        / | \\
     |          |
     |         / \\
     |       _/   \\_
     |
  ___|___''']      

        current_lives = self.lives - self.num_wrong_guesses
        LIFE_STR_SINGULAR = "life"
        LIFE_STR_PLURAL = "lives"
        LIFE_STR = LIFE_STR_SINGULAR if current_lives == 1 else LIFE_STR_PLURAL
        print("Your current state of demise: \n"
            f"You have {current_lives} {LIFE_STR} left")
        if self.lives == self.EASY_LIVES:
            print(HANGMAN_STAGES[self.num_wrong_guesses])
        elif self.lives == self.MEDIUM_LIVES:
            print(HANGMAN_STAGES[self.num_wrong_guesses * 2])
        elif self.lives == self.HARD_LIVES:
            print(HANGMAN_STAGES[self.num_wrong_guesses * 4])

    def validate_guess(self, guess):
        """Validates if guess is a valid character (a-z)

        Parameters:
        guess -- string inputted by user

        Returns: bool, True if guess is valid, else False"""
        if len(guess) == 1 and guess.isalpha():
            if guess in self.letters_guessed:
                print(f"You have already guessed the letter {guess}.")
                return False
            else:
                return True
        else:
            print("That was an invalid guess.")
            return False
            
    def check_guess(self, letter):
        """Updates guessed_word to show all instances of letter

        Parameters:
        letter -- string, character that user guessed

        Returns: int, number of times the letter is in the hidden word
        """
        count = 0
        index = 0
        for character in self.hidden_word:
            if character == letter:
                self.guessed_word = self.guessed_word[:index] + letter + \
                    self.guessed_word[index + 1:]
                count += 1
            index += 1
        return count

    def print_spaced_characters(self, word):
        """Prints a word with spaces between each letter followed by a newline

        Parameters:
        word -- string

        Returns: None
        """
        for character in word:
            print(character, end=' ')
        print()

    def select_difficulty(self):
        """User selects the difficulty, determining how many lives they get

        Returns: none"""
        EASY_STR = "Easy"
        MEDIUM_STR = "Medium"
        HARD_STR = "Hard"

        while True:
            difficulty = input("Please select a difficulty level:\n"
                                "Type E for Easy\nType M for Medium\n"
                                "Type H for Hard\n")
            if difficulty == self.EASY:
                self.lives = self.EASY_LIVES
                difficulty = EASY_STR
                break
            elif difficulty == self.MEDIUM:
                self.lives = self.MEDIUM_LIVES
                difficulty = MEDIUM_STR
                break
            elif difficulty == self.HARD:
                self.lives = self.HARD_LIVES
                difficulty = HARD_STR
                break
            else:
                print("That was an invalid difficulty selection.")
        print(f"Difficulty level {difficulty} selected.\n"
            f"You have {self.lives} lives to free yourself")

    def select_category(self):
        """Player selects the category and a hidden word is chosen"""
        while (True):
            category = input("Please choose a category: \n"
                f"Type {self.CATEGORY_ANIMALS} for animals\n"
                f"Type {self.CATEGORY_HP} for Harry Potter\n"
                f"Type {self.CATEGORY_VEGETABLES} for vegetables\n"
                f"Type {self.CATEGORY_WINTER} for winter\n")
            if category == self.CATEGORY_ANIMALS:
                words = animal_words
                self.category = "animals"
                break
            elif category == self.CATEGORY_HP:
                words = harry_potter_words
                self.category = "Harry Potter"
                break
            elif category == self.CATEGORY_VEGETABLES:
                words = vegetable_words
                self.category = "vegetables"
                break
            elif category == self.CATEGORY_WINTER:
                words = winter_words
                self.category = "winter"
                break
            else:
                print("Invalid category selction.\n")

        word_index = randint(0, len(words) - 1)
        self.hidden_word = words[word_index].lower()
        self.guessed_word = '_' * len(self.hidden_word)

    def player_lost(self):
        """Checks if player lost the game and initiates 

        Returns: Bool, True if lost, else False"""
        if self.lives == self.num_wrong_guesses:
            print(f'You lost! The hidden word was {self.hidden_word}\n'
                f'You had guessed {self.right_character_count} correct letter'
                f'{"" if self.right_character_count == 1 else "s"}:')
            self.print_spaced_characters(self.guessed_word)
            self.player_loses()
            return True

        return False

    def setup_game(self):
        """Sets up a new game"""
        self.letters_guessed = []
        self.hidden_word = ""
        self.guessed_word = ""
        self.num_wrong_guesses = 0
        self.turn = 0
        self.lives = 0
        self.right_character_count = 0
        self.select_category()
        self.select_difficulty()

    def play_game(self):
        """Sets up a new game and checks player's guesses"""
        super().play_game()
        self.setup_game()

        # guess a letter
        while self.num_wrong_guesses < self.lives:
            print(f"Category: {self.category}\n"
                "You are trying to decode: ")
            self.print_spaced_characters(self.guessed_word)
            if len(self.letters_guessed) > 0:
                print("You have guessed: ")
                self.print_spaced_characters(self.letters_guessed)
            guess = input("Guess a letter: ").lower()
            while not self.validate_guess(guess):
                guess = input("Please guess a letter: ")

            self.letters_guessed.append(guess)
            self.letters_guessed.sort()

            right_characters = self.check_guess(guess)

            if not right_characters:
                self.num_wrong_guesses += 1
                print("WRONG!")
            else:
                self.right_character_count += right_characters
                print("Right!")
                if self.right_character_count == len(self.hidden_word):
                    print("You won! You correctly guessed the word "
                    f"{self.hidden_word} in {self.turn} turns!")
                    self.player_wins()
                    break

            self.print_hangman()
            if self.player_lost():
                break
            self.turn += 1

