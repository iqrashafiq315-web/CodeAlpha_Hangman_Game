import random

words = ["physics", "skydriving", "tourism", "friends", "algebra"]
word = random.choice(words)

guessed_letters = []
guesses_left = 6

print("Welcome to Hangman!")
print("You have 6 guesses.\n")

while guesses_left > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!\n")
    else:
        guesses_left -= 1
        print("Wrong! Guesses left:", guesses_left, "\n")

if guesses_left == 0:
    print("Game Over! The word was:", word)