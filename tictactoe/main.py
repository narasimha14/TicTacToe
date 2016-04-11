import random
from board import Board
from randomai import RandomAI
from pseudorandomai import PseudoRandomAI
from humanai import HumanAI
from tictactoe import TicTacToe

if __name__ == "__main__":
  while True:
    board = Board()
    ttt = TicTacToe()
    print "Choose the match-up:"
    print "Type 1 for Random AI v/s Pseudo Random AI"
    print "Type 2 for Pseudo Random AI v/s Pseudo Random AI"
    print "Type 3 for Random AI v/s You"
    print "Type 4 for Pseudo Random AI v/s You"
    print "Type 5 for a 2 player game"
    choice = int( raw_input( "Type in your choice: "))
    if choice == 1:
      ttt.start(board, RandomAI(), PseudoRandomAI())
    elif choice == 2:
      ttt.start(board, PseudoRandomAI(), PseudoRandomAI())
    elif choice == 3:
      humanPlayer = HumanAI()
      ttt.start(board, RandomAI(), humanPlayer)
    elif choice == 4:
      humanPlayer = HumanAI()
      ttt.start(board, humanPlayer, PseudoRandomAI())
    elif choice == 5:
      humanPlayer1 = HumanAI()
      humanPlayer2 = HumanAI()
      humanPlayer1.setName("Player 1")
      humanPlayer2.setName("Player 2")
      ttt.start(board, humanPlayer1, humanPlayer2)

    restart = raw_input("Do you want to try again (Y or N) ?")
    if ( not restart.lower().startswith('y')):
      break
      


