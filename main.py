import string
import random
deck = {
  "Ace of Diamonds":1,
  "King of Diamonds":13,
  "Queen of Diamonds":12,
  "Jack of Diamonds":11,
  "10 of Diamonds":10,
  "9 of Diamonds":9,
  "8 of Diamonds":8,
  "7 of Diamonds":7,
  "6 of Diamonds":6,
  "5 of Diamonds":5,
  "4 of Diamonds":4,
  "3 of Diamonds":3,
  "2 of Diamonds":2,
  "Ace of Clubs":1,
  "King of Clubs":13,
  "Queen of Clubs":12,
  "Jack of Clubs":11,
  "10 of Clubs":10,
  "9 of Clubs":9,
  "8 of Clubs":8,
  "7 of Clubs":7,
  "6 of Clubs":6,
  "5 of Clubs":5,
  "4 of Clubs":4,
  "3 of Clubs":3,
  "2 of Clubs":2,
  "Ace of Hearts":1,
  "King of Hearts":13,
  "Queen of Hearts":12,
  "Jack of Hearts":11,
  "10 of Hearts":10,
  "9 of Hearts":9,
  "8 of Hearts":8,
  "7 of Hearts":7,
  "6 of Hearts":6,
  "5 of Hearts":5,
  "4 of Hearts":4,
  "3 of Hearts":3,
  "2 of Hearts":2,
  "Ace of Spades":1,
  "King of Spades":13,
  "Queen of Spades":12,
  "Jack of Spades":11,
  "10 of Spades":10,
  "9 of Spades":9,
  "8 of Spades":8,
  "7 of Spades":7,
  "6 of Spades":6,
  "5 of Spades":5,
  "4 of Spades":4,
  "3 of Spades":3,
  "2 of Spades":2
}
while True:
  BIG_CHOICE = input("New Hand (N) or Quit Game (G): ")
  if BIG_CHOICE == "G" or str.lower(BIG_CHOICE) == "q":
    break
  elif BIG_CHOICE == "N" or str.lower(BIG_CHOICE) == "n":
    HAND = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
    print("Your current hand is: " + HAND[0] + " & " + HAND[1])
