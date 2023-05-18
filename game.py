import random
import time

name = input("What is your name? ")
print("Welcome, " + name + "! Let's play the word guessing game.")

file = open('words.txt', 'r')
words = file.read().split()
file.close()

def display_word(word, guesses):
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
    print()

def get_valid_guess(guesses):
    while True:
        guess = input("\nGuess a character: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guesses:
            print("You have already guessed that character. Try again.")
        else:
            return guess

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def display_hangman(turns):
    hangman = [
        '''
          +---+
              |
              |
              |
             ===
        ''',
        '''
          +---+
          O   |
              |
              |
             ===
        ''',
        '''
          +---+
          O   |
          |   |
              |
             ===
        ''',
        '''
          +---+
          O   |
         /|   |
              |
             ===
        ''',
        '''
          +---+
          O   |
         /|\\  |
              |
             ===
        ''',
        '''
          +---+
          O   |
         /|\\  |
         /    |
             ===
        ''',
        '''
          +---+
          O   |
         /|\\  |
         / \\  |
             ===
        '''
    ]
    max_turns = len(hangman) - 1
    display_stage = min(turns, max_turns)
    print(hangman[display_stage])


# Game loop
play_game = True
while play_game:
    # Choose a random word
    word = random.choice(words).lower()
    word_length = len(word)

    print("\nLet's begin! The word has", word_length, "characters.")

    guesses = []
    turns = 7
    score = 0

    while turns > 0:
        print("\nCurrent Score:", score)
        display_word(word, guesses)
        display_hangman(turns)

        guess = get_valid_guess(guesses)
        guesses.append(guess)

        if guess in word:
            print("Correct guess!")
            score += 1
        else:
            print("Wrong guess!")
            turns -= 1

        if all(char in guesses for char in word):
            print("Congratulations, you won!")
            print("The word is:", word)
            break

    if turns == 0:
        print("Oops! You ran out of turns.")
        print("The word was:", word)

    play_game = play_again()

print("Thank you for playing. Goodbye!")
