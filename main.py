import os
import random

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += f"{letter} "
    else:
      display += "_ "
  print(f"{display}\n")

  display = ""
  for letter in alphabet:
    if letter in guessed_letters:
      display += " "
    else:
      display += letter
  print(f"{display}\n")

  print(f"Guesses left: {guesses_left}\n")

def get_letter():
  while True:
    letter = input("Which letter? ").lower()

    if letter == "" or letter not in alphabet:
      print("Choose a-z.\n")
    elif letter in guessed_letters:
      print(f"{letter} has already been guessed.\n")
    else:
      return letter

def word_guessed():
  return all(letter in guessed_letters for letter in word)

dictionary = [
  "code",
  "variable",
  "function",
  "operator",
  "comment",
  "print",
  "string",
  "integer",
  "float",
  "import",
  "condition",
  "logic",
  "true",
  "false",
  "parameter",
  "loop",
  "increment",
  "list",
  "index",
  "dictionary",
]

alphabet = "abcdefghijklmnopqrstuvwxyz"

word = random.choice(dictionary)
guessed_letters = []
guesses_left = 7
game_over = False

while not game_over:
  print_game_state()

  letter = get_letter()
  guessed_letters.append(letter)

  if letter not in word:
    guesses_left -= 1

  if word_guessed():
    game_over = True
    print_game_state()
    print("You win!")
  elif guesses_left == 0:
    game_over = True
    print_game_state()
    print(f"You lose. The word was {word}.")
