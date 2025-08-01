import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'orange', 'grape']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while True:
        # Display current word state
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord: " + ' '.join(display_word))

        # Check if player has won
        if '_' not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break

        # Get player's guess
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add guess to guessed letters
        guessed_letters.add(guess)

        # Check if guess is correct
        if guess not in word:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect - incorrect_guesses} guesses left.")

        # Check if player has lost
        if incorrect_guesses >= max_incorrect:
            print(f"Game over! The word was '{word}'.")
            break

if __name__ == "__main__":
    hangman()
