import unittest
from board import Board
from pseudorandomai import PseudoRandomAI

class TestBoard(unittest.TestCase):
  """ 
  Tests if the board is empty 
  """
  def testEmptyBoard(self):
    board = Board()
    self.assertEqual(board.isEmpty(), True)
    board.makeMove(0, 'X')
    self.assertEqual(board.isEmpty(), False)

  """ 
  Tests if the given space is free on the board 
  """
  def testIsSpaceFree(self):
    board = Board()
    board.makeMove(5, 'O')
    self.assertEqual(board.isSpaceFree(5), False)

  """ 
  Tests if the player with the specified letter has won the board 
  """
  def testWinner(self):
    board = Board()
    board.makeMove(0,'X')
    board.makeMove(1,'X')
    board.makeMove(2,'X')
    self.assertEqual(board.isWinner('X'), True)

  """ 
  Tests if the specified move is invalid
  """
  def testInvalidMove(self):
    board = Board()
    board.makeMove(0,'X')
    self.assertEqual( board.makeMove(0,'X'), False)

  """
  Tests if the board is full
  """
  def testBoardFull(self):
    board = Board()
    for i in range(9):
      board.makeMove(i,'X')
    self.assertEqual(board.isFull(), True)

class TestAI(unittest.TestCase):
  """ 
  Tests the next move returned by the AI 
  """
  def testNextMove(self):
    ai = PseudoRandomAI()
    # If corners are free, choose the corners
    board = Board()
    self.assertIn(ai.getNextMove(board,'X'), [0,2,6,8])
    board.makeMove(0,'X')
    board.makeMove(1,'O')
    board.makeMove(2,'X')
    board.makeMove(6,'O')
    self.assertEqual(ai.getNextMove(board, 'X'), 8)
    # If corners, aren't free, choose the center if free
    board.makeMove(8,'X')
    self.assertEqual(ai.getNextMove(board, 'X'), 4)
    # If center is not free, choose any other
    board.makeMove(4,'O')
    self.assertIn(ai.getNextMove(board,'X'), [1,3,5,7])

  """ 
  Tests if the getNextMove returns None if all the spaces are filled 
  """
  def testNoMove(self):
    ai = PseudoRandomAI()
    board = Board()
    board.makeMove(0,'X')
    board.makeMove(1,'O')
    board.makeMove(2,'X')
    board.makeMove(3,'O')
    board.makeMove(4,'X')
    board.makeMove(5,'O')
    board.makeMove(6,'X')
    board.makeMove(7,'O')
    board.makeMove(8,'X')
    self.assertEqual(ai.getNextMove(board, 'X'), None)

