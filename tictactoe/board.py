from copy import deepcopy

class Board:
  def __init__(self):
    self.squares = [' ']*9
    print len(self.squares)

  def printBoard(self):
    print ""
    print('   |   |')
    print(' ' + self.squares[0] + ' | ' + self.squares[1] + ' | ' + self.squares[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + self.squares[3] + ' | ' + self.squares[4] + ' | ' + self.squares[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + self.squares[6] + ' | ' + self.squares[7] + ' | ' + self.squares[8])
    print('   |   |')
    print ""
  def isSpaceFree(self, number):
    return (self.squares[number] == ' ')

  def makeMove(self, number, letter):
    if self.squares[number] == ' ':
      self.squares[number] = letter
      return True
    else:
      return False

  def getBoard(self):
    return deepcopy(self)
  
  def isFull(self):
    for i in range(9):
      if self.isSpaceFree(i):
        return False
    return True

  def isEmpty(self):
    for i in range(9):
      if not self.isSpaceFree(i):
        return False
    return True

  def isWinner(self, letter):
    return ((self.squares[6] == letter and self.squares[7] == letter and self.squares[8] == letter) or # across the top
    (self.squares[3] == letter and self.squares[4] == letter and self.squares[5] == letter) or # across the middle
    (self.squares[0] == letter and self.squares[1] == letter and self.squares[2] == letter) or # across the self.squaresttom
    (self.squares[0] == letter and self.squares[3] == letter and self.squares[6] == letter) or # down the left side
    (self.squares[1] == letter and self.squares[4] == letter and self.squares[7] == letter) or # down the middle
    (self.squares[2] == letter and self.squares[5] == letter and self.squares[8] == letter) or # down the right side
    (self.squares[0] == letter and self.squares[4] == letter and self.squares[8] == letter) or # diagonal
    (self.squares[6] == letter and self.squares[4] == letter and self.squares[2] == letter))
