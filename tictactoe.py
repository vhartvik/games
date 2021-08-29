from random import randint

from game import Game

class TicTacToe(Game):
	def __init__(self, name, game_intro):
		super().__init__(name, game_intro)
		self.board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
		self.player_order = 1
		self.player_symbol = "X"
		self.computer_symbol = "O"
		self.winner = ""

	def setup_game(self):
		"""Setup board game

		Returns: None"""
		self.board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
		self.player_order = randint(1, 2)
		if self.player_order == 1:
			self.player_symbol = "X"
			self.computer_symbol = "O"				
		else:
			self.player_symbol = "O"
			self.computer_symbol = "X"	
		self.winner = ""

	def print_board(self):
		"""Prints tic tac toe game board

		Returns: None"""
		print(
			"   |   |   \n"
			f" {self.board[1]} | {self.board[2]} | {self.board[3]} \n"
			"___|___|___\n"
			"   |   |   \n"
			f" {self.board[4]} | {self.board[5]} | {self.board[6]} \n"
			"___|___|___\n"
			"   |   |   \n"
			f" {self.board[7]} | {self.board[8]} | {self.board[9]} \n"
			"   |   |   \n")

	def is_game_over(self):
		"""Checks if a player has gotten 3 tiles in a row, column, or diagonal

		Returns: bool, True if game is over, else False"""
		if (self.board[1] == self.computer_symbol and \
			self.board[2] == self.computer_symbol and \
			self.board[3] == self.computer_symbol) or (
			self.board[4] == self.computer_symbol and \
			self.board[5] == self.computer_symbol and \
			self.board[6] == self.computer_symbol) or (
			self.board[7] == self.computer_symbol and \
			self.board[8] == self.computer_symbol and \
			self.board[9] == self.computer_symbol) or (
			self.board[1] == self.computer_symbol and \
			self.board[4] == self.computer_symbol and \
			self.board[7] == self.computer_symbol) or (
			self.board[2] == self.computer_symbol and \
			self.board[5] == self.computer_symbol and \
			self.board[8] == self.computer_symbol) or (
			self.board[3] == self.computer_symbol and \
			self.board[6] == self.computer_symbol and \
			self.board[9] == self.computer_symbol) or (
			self.board[1] == self.computer_symbol and \
			self.board[5] == self.computer_symbol and \
			self.board[9] == self.computer_symbol) or (
			self.board[3] == self.computer_symbol and \
			self.board[5] == self.computer_symbol and \
			self.board[7] == self.computer_symbol):
			self.winner = self.computer_symbol
			return True
		elif (self.board[1] == self.player_symbol and \
			self.board[2] == self.player_symbol and \
			self.board[3] == self.player_symbol) or (
			self.board[4] == self.player_symbol and \
			self.board[5] == self.player_symbol and \
			self.board[6] == self.player_symbol) or (
			self.board[7] == self.player_symbol and \
			self.board[8] == self.player_symbol and \
			self.board[9] == self.player_symbol) or (
			self.board[1] == self.player_symbol and \
			self.board[4] == self.player_symbol and \
			self.board[7] == self.player_symbol) or (
			self.board[2] == self.player_symbol and \
			self.board[5] == self.player_symbol and \
			self.board[8] == self.player_symbol) or (
			self.board[3] == self.player_symbol and \
			self.board[6] == self.player_symbol and \
			self.board[9] == self.player_symbol) or (
			self.board[1] == self.player_symbol and \
			self.board[5] == self.player_symbol and \
			self.board[9] == self.player_symbol) or (
			self.board[3] == self.player_symbol and \
			self.board[5] == self.player_symbol and \
			self.board[7] == self.player_symbol):
			self.winner = self.player_symbol
			return True
		return False

	def validate_number_selection(self, selection):
		"""Checks if a tile is available to be selected

		Parameters:
		selection -- int, tile being selected

		Returns: bool, True if available, else False"""
		return self.board[selection] != self.computer_symbol and \
			self.board[selection] != self.player_symbol

	def validate_selection(self, selection):
		"""Checks that user's selection is a valid quadrant

		Parameters:
		selection -- string, tile being selected

		Returns: bool, True if selected tile is allowed, else False"""
		if len(selection) == 1 and selection.isdigit():
			return self.validate_number_selection(int(selection))
		return False

	def computer_turn(self):
		"""Computer makes a move

		Returns: None"""
		selection_order = [5, 1, 9, 7, 3, 4, 1, 6, 8]
		selection = selection_order[0]
		while not self.validate_number_selection(selection):
			selection_order.pop(0)
			selection = selection_order[0]
		print("The computer placed their "
			f"{self.computer_symbol} in tile {selection}")
		self.board[selection] = self.computer_symbol
		self.print_board()

	def user_turn(self):
		"""User makes a move

		Returns: None"""
		print("It's your turn")
		print(f"You are {self.player_symbol}s\n")
		self.print_board()
		while True:
			selection = input("Type in a number to place your "
				f"{self.player_symbol} in that tile ")
			if self.validate_selection(str(selection)):
				print(f"You selected Tile {selection}")
				self.board[int(selection)] = self.player_symbol
				self.print_board()
				break
			else:
				print("Invalid selection. Please try again.")

	def play_game(self):
		"""Setup game and ask player for 

		Returns: None"""
		super().play_game()
		self.setup_game()

		game_is_over = False
		turn = 0
		while(not game_is_over):
			if self.player_order == 1 and turn % 2 == 0 or (
				self.player_order == 2 and turn % 2 != 0):
				self.user_turn()
			else:
				self.computer_turn()
			game_is_over = self.is_game_over()
			turn += 1

		if self.winner == self.computer_symbol:
			print(f"The computer, player {self.computer_symbol} wins!")
			self.print_board()
			super().player_loses()
		else:
			print(f"You did it! {self.player_symbol} wins!")
			self.print_board()
			super().player_wins()


