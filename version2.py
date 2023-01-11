# A redone, better version of rock paper scissors with better coding practices

from random import randint
from time import sleep

options = ["Rock", "Paper", "Scissors"]
optionLength = 3

LOSS_STRING = "You lost!"
TIE_STRING = "It's a tie!"
WIN_STRING = "You won!"

def computeWinner(userIndex, computerIndex):
  print "You selected: %s" % options[userIndex]
  sleep(1)
  
  print "Computer selected: %s" % options[computerIndex]
  
  if userIndex == computerIndex:
    print TIE_STRING
  elif userIndex == 0 and computerIndex == 2:
    print WIN_STRING
  elif userIndex == 1 and computerIndex == 0:
    print WIN_STRING
  elif userIndex == 2 and computerIndex == 1:
    print WIN_STRING
    return
  else:
    print LOSS_STRING
        
def playGame():
  print "Rock, Paper, or Scissors?"
  try
    userChoice = raw_input()
    userIndex = options.index(userChoice)
  except ValueError
    print "Only Choose Rock, Paper, or Scissors!"
    playGame()
  else
    sleep(1)
    computerIndex = randint(0, optionLength -1)
    computeWinner(userIndex, computerIndex)

playGame()
