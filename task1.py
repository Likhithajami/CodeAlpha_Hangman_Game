import random

print("====== HANGMAN GAME ======")

words = ["python", "tiger", "apple", "music", "chair"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You Won")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:

        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("Correct Guess")

        else:
            print("Letter already guessed")

    else:
        wrong_guesses += 1
        print("Wrong Guess")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

if wrong_guesses == max_wrong_guesses:
    print("\nGame Over")
    print("Correct Word is:", word)

print("\nThank You For Playing")