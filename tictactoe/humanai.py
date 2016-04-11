from ai import AI

class HumanAI(AI):
  name = "You"
  def setName(self, name):
    self.name = name
  def getName(self):
    return self.name
  def getNextMove(self, board, letter):
    while True:
      move = int(raw_input("Enter the position for your move [1-9]: ") )
      if move < 1 or move > 9:
        print "Not a valid move"
      else:
        if board.isSpaceFree(move-1):
          return move-1
        else:
          print "Not a valid move"
    return None
