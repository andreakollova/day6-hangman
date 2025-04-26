import random
#1 RANDOM WORD IS GENERATED AND PRINTED, ALSO SPLIT INTO LETTERS
word_list = ["apple", "house", "table", "chair", "river", "stone", "cloud", "beach", "smile", "music", "grass", "water", "bread", "light", "flower", "heart", "dream", "honey", "orange", "sunny"]

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
guess = input("Guess a letter: ")

# 3 IF THE LETTER IS IN THE WORD, THE LETTER THERE
display = ""
for letter in letters:
    if guess == letter:
        display += letter
    else:
        display += "_"
print(display)