import random

name = input("What is your name? ")
print("Good Luck !", name)

file = open('words.txt', 'r')
words = file.read().split()

# Function will choose one random and convert to lowercase
# word from this list of words
word = random.choice(words).lower()

print("Guess the characters")

guesses = ''

turns = 10

while turns > 0:

    # counts the number of times a user fails
    fail = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=' ')

        else:
            print("_", end=' ')

            # for every failure 1 will be incremented in failure
            fail += 1

    if fail == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print("The word is:", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("\nguess a character:")
    print("========================")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose"), print("Word is:", word)
