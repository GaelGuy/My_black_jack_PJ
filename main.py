############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
from art import logo
from replit import clear

#def drawn_card():
player_card = []
com_card = []
com_display = []
a_card = []

cards = {"A":11,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 10,"Q": 10,"K": 10}

def drawn_card(deck):
  for card in deck:
    a_card.append(card)
  return random.choice(a_card)

def score_count(deck,card_in_hand):
  score = 0
  for i in card_in_hand:
    score += deck[i]
  return score
  
def Display1(player_card,deck,com_display,com_card):
  print(logo) 
  print(f"your cards : {player_card} \nScore {score_count(cards,player_card)}")
  print(f"oppenent cards : {com_display}\nScore {score_count(cards,com_display[1])}")
  
def Display2(player_card,deck,com_display,com_card):
  print(logo) 
  print(f"your cards : {player_card} \nScore {score_count(cards,player_card)}")
  print(f"oppenent cards : {com_card}\nScore {score_count(cards,com_card)}")

def start_game():
  game = True
  player = False
  oppenent = False
  player_turn = True
  com_turn = True
  for i in range(2):
    player_card.append(drawn_card(cards))
    com_card.append(drawn_card(cards))
    com_display.append("X")
    
  com_display[1] = com_card[1]
  Display1(player_card,cards,com_display,com_card)
  #Start play!!!!!
  while game:
    # Player action phase
    while player_turn:
      if score_count(cards,player_card) == 21:
        player = True
        print("Black jack")
        if score_count(cards,com_card) < 17:
          com_card.append(drawn_card(cards))
          clear()
          Display2(player_card,cards,com_display,com_card)
        elif score_count(cards,com_card) > 17:
          print(com_card)
          player_turn = False
          com_turn = False
          player = True
          if score_count(cards,com_card) == 21:
            oppenent = True
      elif score_count(cards,player_card) > 21:
        oppenent = True
        player_turn = False
        com_turn = False
        clear()
        Display2(player_card,cards,com_display,com_card)
      else:
        # Player select the action
        selection = input("Enter 'Hit' to drawn card 'Stand'to challent : ").title()
        if selection == "Hit":
          player_card.append(drawn_card(cards))
          clear()
          Display1(player_card,cards,com_display,com_card)
        elif selection == "Stand":
          player_turn = False
    #Computer action phase
    while com_turn:
      if score_count(cards,com_card) == 21:
        oppenent = True
        com_turn = False
        clear()
        Display2(player_card,cards,com_display,com_card)
      elif score_count(cards,com_card) < 17:
        com_card.append(drawn_card(cards))
        clear()
        Display2(player_card,cards,com_display,com_card)
      elif score_count(cards,com_card) >= 17:
        clear()
        Display2(player_card,cards,com_display,com_card)
        if score_count(cards,com_card) > 21:
          player = True
        com_turn = False
    score_com = score_count(cards,com_card)  
    score_player = score_count(cards,player_card)
    clear()
    Display2(player_card,cards,com_display,com_card)
    if not player and not oppenent:
      if score_com > score_player:
        oppenent = True
      elif score_player > score_com:
        player = True
      else:
        oppenent = True
        player = True
        
    if player and oppenent:
      print("DRAW")
    elif oppenent:
      print("You Lose")
    elif player:
      print("You Win")

    game = False

start_game()       
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

