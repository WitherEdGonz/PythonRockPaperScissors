import random
import numpy
from tkinter import *

#list of variable we may use
global player1Choice
global player2Choice
global gameTypeChoice

def rockArt():
  print("   _ _ _ _\n  |_|_|_|_|\n _| | | | |\n(         |\n(         |\n(_________|")

def paperArt():
  print("   _ _ _ _\n  | | | | |\n  | | | | |\n _|_|_|_|_|\n(         |\n(_________|")

def scissorsArt():
  print("   _ _\n  |_|_|\n  | | |_ _\n _| | | | |\n(         |\n(_________|")

def gameType():
  while True:
    print("Welcome to ROCK-PAPER-SCISSORS SHOWDOWN!!1!")
    print("Would you like to play against a computer or against another player?")
    print("1: Vs. Computer")
    print("2: Vs. Player")
    print("3: Quit")

    rockArt()
    paperArt()
    scissorsArt()
    

    gameTypeChoice = input()
    if gameTypeChoice == "1":
      computerVsPlayer()
      break
    elif gameTypeChoice == "2":
      playerVsPlayer()
      break
    elif gameTypeChoice == "3":
      exit()
      break
    else:
      print("That's an invalid choice. Please try again.\n")

def playerChoiceRestart(gamemode):
  print("Would you like to play again?")
  print("1: Yes")
  print("2: Restart Program")
  print("3: Quit")
  restartChoice = input()
  if restartChoice == "1":
    if gamemode == 0: computerVsPlayer()
    else: playerVsPlayer()
  elif restartChoice == "2": 
    gameType()
  elif restartChoice == "3": 
    exit()
  else:
    print("That's an invalid choice. Please try again.\n")

def playerChoice():
  while True:
    print("\n1: Rock")
    print("2: Paper")
    print("3: Scissors")
    rpsChoice = input()
    if rpsChoice in ["1","2","3"]:
      return rpsChoice
    print("That's an invalid choice. Please try again.")

def computerChoice():
    return str(random.randint(1,3))

def compareChoices(p1Choice, p2Choice, gamemode):
  secondPlayerDict = {
    0: "Computer",
    1: "Player 2"
  }
  secondPlayer = secondPlayerDict.get(gamemode, "Player 2")
  if p1Choice == p2Choice:
    print("It's a tie! There are no ties in RPS! Go again!")
    if secondPlayer == "Computer":
      computerVsPlayer()
    else:
      playerVsPlayer()
  else:
    if p1Choice == "1":
      if p2Choice == "2":
        print("Paper covers rock! {} wins!\n".format(secondPlayer))
      elif p2Choice == "3":
        print("Rock crushes scissors! Player 1 wins!\n")
    elif p1Choice == "2":
      if p2Choice == "1":
        print("Paper covers rock! Player 1 wins!\n")
      elif p2Choice == "3":
        print("Scissors cuts paper! {} wins!\n".format(secondPlayer))
    elif p1Choice == "3":
      if p2Choice == "1":
        print("Rock crushes scissors! {} wins!\n".format(secondPlayer))
      elif p2Choice == "2":
        print("Scissors cuts paper! Player 1 wins!\n")
    playerChoiceRestart(gamemode)

def computerVsPlayer():
  print("\nPlayer 1, make your choice!")
  player1Choice = playerChoice()
  compareChoices(player1Choice, computerChoice(), 0)

def playerVsPlayer():
  print("\nPlayer 1, make your choice!")
  player1Choice = playerChoice()
  print("Player 2, make your choice!")
  player2Choice = playerChoice()
  compareChoices(player1Choice, player2Choice, 1)

gameType()
