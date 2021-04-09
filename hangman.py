from random import choice


def choose_word():
    """Chooses a random word out of a list of words located in the words.txt file"""
    lines = open("words.txt").read().splitlines()
    random_word = choice(lines)

    return random_word


print("Welcome to Hangman! A random word is chosen for you, and it is your job to guess!")
word = choose_word()  # choose random word

output = "_" * len(word)
word_guess = list(output)
already_guessed = []  # keeps track of what the player has already guessed to avoid re-guessing
wrong_guess = 10  # number of allowed guesses

while wrong_guess > 0:
    print("".join(word_guess))
    if "".join(word_guess) == word:
        print(f'You guessed it! Great job! The final answer is: {word}!')
        break
    guess = input("Guess a letter or the word: ").lower()  # guesses are case insensitive
    while guess in already_guessed:
        print(f"Your guesses: {already_guessed}")
        guess = input("You already guessed that, try again. Guess a letter or the word: ").lower()

    already_guessed.append(guess)

    if len(guess) == 1:  # single character guess
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_guess[i] = guess
        else:
            wrong_guess -= 1
            print(f"That letter is not in the word. Incorrect Guesses left: {wrong_guess}")

    else:  # full word guess
        if guess.lower() == word:
            print(f'You guessed it! Great job! The final answer is: {word}!')
            break
        else:
            wrong_guess -= 1
            print(f"That is not the word. Incorrect Guesses left: {wrong_guess}")

if wrong_guess == 0:
    print(f"Out of guesses! The word was {word}")
