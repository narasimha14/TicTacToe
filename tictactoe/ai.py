from abc import ABCMeta, abstractmethod

class AI:
  @abstractmethod
  def getNextMove(self, board, letter):
    """ Returns the next position of placement of the letter for the player """

  @abstractmethod
  def getName(self):
    """ Returns the name of the AI """
