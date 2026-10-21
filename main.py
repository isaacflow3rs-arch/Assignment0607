#import functions, prepare lists
from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

#welcoming and selecting secret word, resetting previous guesses, play again loop

while True:

    previous_guesses = []
    guess_count = 0

    print("------- Welcome to Wordle Clone! -------")
    print("In this game, you will get 6 guesses to help you find the secret word.\n" \
        "Each guess will give you clues until you figure it out. Good luck!")
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word\n\n")

    secret_word = choose_word()

    #collecting guesses, tracking # of guesses
    while guess_count < 6:
        print(f"Guess {guess_count + 1}/6:")
        player_guess = get_guess(previous_guesses)
        guess_count += 1

        feedback = evaluate_guess(secret_word, player_guess)

        display_guess(feedback, player_guess)

        #determining if won
        if has_won(player_guess, secret_word):
            if guess_count == 1:
                print(f"Nice work! The word was {secret_word}. You found it in {guess_count} try!\n")
            else:
                print(f"Nice work! The word was {secret_word}. You found it in {guess_count} tries!\n")
            break

        elif guess_count == 6:
            print(f"Better luck next time. The secret word was {secret_word}.\n\n")

    #play again option
    if input("Play again? (y/n) ").lower().strip() != "y":
        print("Thanks for playing!")
        break