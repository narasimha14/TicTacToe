import random

class TicTacToe:
  # Default constructor to assign the letters
  def __init__(self):
    self.letter1 = "X"
    self.letter2 = "O"

  # Function to print the player that goes first
  def printGoFirst(self, player):
    name = player.getName()
    if name == "You":
      print player.getName(), "go first with letter", self.letter1
    else:
      print player.getName() , "goes first with letter" , self.letter1

  # Function to print the winner
  def printWinner(self, player):
    winner = player.getName()
    if winner == "You":
      print player.getName(), "have won the game"
    else:
      print player.getName(), "has won the game"

  # Start of the game
  def start(self, board, player1, player2):
    # Check to see who goes first
    if random.randint(0, 1) == 0:
      self.printGoFirst(player1)

      while True:
        # Make a move and check if that move wins/draws the game
        board.makeMove( player1.getNextMove(board, self.letter1), self.letter1)
        board.printBoard()
        if board.isWinner(self.letter1):
          self.printWinner(player1)
          break
        if board.isFull():
          print "The game is drawn"
          break

        # Make a move and check if that move wins/draws the game
        board.makeMove( player2.getNextMove(board, self.letter2), self.letter2)
        board.printBoard()
        if board.isWinner(self.letter2):
          self.printWinner(player2)
          break
        if board.isFull():
          print "The game is drawn" 
          break
    else:
      self.printGoFirst(player2)

      while True:
        # Make a move and check if that move wins/draws the game
        board.makeMove( player2.getNextMove(board, self.letter1), self.letter1)
        board.printBoard()
        if board.isWinner(self.letter1):
          self.printWinner(player2)
          break
        if board.isFull():
          print "The game is drawn"
          break

        # Make a move and check if that move wins/draws the game
        board.makeMove( player1.getNextMove(board, self.letter2), self.letter2)
        board.printBoard()
        if board.isWinner(self.letter2):
          self.printWinner(player1)
          break
        if board.isFull():
          print "The game is drawn"
          break

