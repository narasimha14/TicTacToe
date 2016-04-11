import random
from ai import AI

class RandomAI(AI):

  def getNextMove(self, board, letter):
    return self.chooseRandomMoveFromList(board, range(9))
 
  def chooseRandomMoveFromList(self, board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if board.isSpaceFree(i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

  def getName(self):
    return "Randomi AI"
