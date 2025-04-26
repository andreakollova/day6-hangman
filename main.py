stages = [r'''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
+---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      | 
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

import random
#1 RANDOM WORD IS GENERATED AND PRINTED, ALSO SPLIT INTO LETTERS
word_list = ["apple", "house", "table", "chair", "river", "stone", "cloud", "beach", "smile", "music", "grass", "water", "bread", "light", "flower", "heart", "dream", "honey", "orange", "sunny"]

lives = 6

random_word = random.choice(word_list)
print(random_word)

letters = list(random_word)
print(letters)

#4 CREATE A PLACEHOLDER WITH THE LENGTH OF THE WORD
word_length = len(random_word)
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#2 USER INPUTS A GUESSED LETTER
gameover = False
correct_letter = []

while not gameover:
    guess = input("Guess a letter: ")

    display = ""
    for letter in letters:
        if guess == letter:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in letters:
        lives -= 1
        if lives == 0:
            gameover = True
            print("You lose!")

    if "_" not in display:
        gameover = True
        print("You won!")

    print(stages[lives])