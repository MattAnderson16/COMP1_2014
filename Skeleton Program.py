# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

######test change#############

import random
import datetime
import pdb

NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = '-'
    self.Score = 0
    self.Date = '-'

Ace = 'low'
EndIfSame = True
Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1 or RankNo == 14:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save high scores')
  print('7. Load high scores')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input().lower()
  print()
  Choice = Choice[0]
  return Choice

def LoadDeck(Deck):
  global Ace
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if Ace == 'high' and Deck[Count].Rank == 1:
      Deck[Count].Rank = 14 
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  global EndIfSame
  Higher = False
  Same = False
  if NextCard.Rank == LastCard.Rank and EndIfSame == False:
    Same = True
  elif NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher,Same

def GetPlayerName():
  GotName = False
  while not GotName:
    print()
    PlayerName = input('Please enter your name: ')
    print()
    if PlayerName == " ":
      print("You need to input a name!")
    else:
      GotName = True
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ').lower()
  Choice = Choice[0]
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = None

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<10}{1:<6}{2:<8}".format("Name","Score","Date"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10}{1:<6}{2:<8}".format(RecentScores[Count].Name,RecentScores[Count].Score, RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  Date = datetime.date.today()
  Date = datetime.datetime.strftime(Date,"%d/%m/%y")
  Valid = False
  while not Valid:
    YesorNo = input("Would you like your name to be added to the recent high scores? y/n ").lower()
    YesoorNo = YesorNo[0]
    if YesorNo in ["y","n","yes","no"]: 
      if YesorNo == "y":
        PlayerName = GetPlayerName()
        Valid = True
      elif YesorNo == "n":
        PlayerName = ""
        Valid = True
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
      RecentScores[Count].Date = RecentScores[Count + 1].Date
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = Date
  return RecentScores

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    Higher,Same = IsNextCardHigher(LastCard, NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    elif ((Higher and Choice == 'n') or (not Higher and Choice == 'y')) and Same:
      print("Oops! the next card was the same value!")
      print()
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def DisplayOptions():
  print()
  print("OPTIONS")
  print()
  print("1. Ace high or low")
  print("2. End game if same card")
  print()
  print("Select an option or press q to quit: ")

def GetOptionChoice():
  Valid = False
  while not Valid: 
    Choice = input().lower()
    Choice = Choice[0]
    if Choice in ['1','2','q']:
      Valid = True
    else:
      print("Please input a valid option")
      print()
  return Choice

def SetOptions(OptionChoice):
  if OptionChoice == '1':
    SetAceHighOrLow()
  elif OptionChoice == '2':
    SetSameScore()

def SetAceHighOrLow():
  global Ace
  print("Would you like the ace to be high or low? ")
  Finished = False
  while not Finished:
    Choice = input().lower()
    print()
    Choice = Choice[0]
    if Choice == "h":
      Ace = "high"
      Finished = True
    elif Choice == "l":
      Ace = "low"
      Finished = True
    else:
      print("Please input a valid choice")

def BubbleSortScores(RecentScores):
##  pdb.set_trace()
  SwapMade = True
  while SwapMade:
    SwapMade = False
    for count in range(1, NO_OF_RECENT_SCORES):
      if RecentScores[count+1].Score > RecentScores[count].Score:
        Temp = RecentScores[count+1]
        RecentScores[count+1] = RecentScores[count]
        RecentScores[count] = Temp
        SwapMade = True

def SaveScores(RecentScores):
  with open("Save_Scores.txt",mode = 'w', encoding = 'utf-8') as MyFile:
    for count in range(1, len(RecentScores)):
      MyFile.write("{0}\n".format(RecentScores[count].Name))
      MyFile.write("{0}\n".format(RecentScores[count].Score))
      MyFile.write("{0}\n".format(RecentScores[count].Date))

def LoadScores():
  global RecentScores
  List = []
  with open("Save_Scores.txt",mode = 'r', encoding = 'utf-8') as MyFile:
    for line in MyFile:
      List.append(line)
  finished = False
  while not finished:
    if List[0] == " ":
      finished = True
    else:
      counter = 1
    ##  pdb.set_trace()
      for count in range(0,3*NO_OF_RECENT_SCORES,3): #len(List) changed to 3*NO_OF_RECENT_SCORES
    ##    TRecentScore.Name = List[count]
    ##    TRecentScore.Score = List[count+1]
    ##    TRecentScore.Date = List[count+2]
        RecentScores[counter].Name = List[count].rstrip("\n")
        RecentScores[counter].Score = List[count+1].rstrip("\n")
        RecentScores[counter].Score = int(RecentScores[counter].Score)
        RecentScores[counter].Date = List[count+2].rstrip("\n")
        counter +=1
      finished = True

def SetSameScore():
  global EndIfSame
  yn = input("Do you want cards of the same value as the previous one to end the game? ").lower()
  while yn not in["y","yes","n","no"]:
    print("Please input a valid response")
    yn = input("Do you want cards of the same value as the previous one to end the game? ").lower() 
  yn = yn[0]
  if yn == "y":
    EndIfSame = True
  elif yn == "n":
    EndIfSame = False

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      Finished = False
      while OptionChoice != 'q' and not Finished:
        SetOptions(OptionChoice)
        Finished = True
    elif Choice == '6':
      SaveScores(RecentScores)
    elif Choice == '7':
      LoadScores()
      
