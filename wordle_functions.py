#imports and preparing word bank

import random

words = [
    "plant", "crane", "slate", "brick", "house",
    "chair", "grape", "flame", "stone", "bread",
    "cloud", "train", "beach", "smile", "light",
    "water", "dream", "paint", "shirt", "mouse",
    "tiger", "horse", "zebra", "snake", "whale",
    "shark", "punch", "robin", "stork", "camel",
    "fruit", "peach", "melon", "lemon", "mango",
    "plums", "grind", "spice", "boast", "honey",
    "sugar", "cream", "drink", "lunch", "feast",
    "table", "bunch", "shelf", "clunk", "radio",
    "phone", "cable", "panel", "brush", "towel",
    "piano", "flute", "drums", "viola", "dance",
    "music", "sound", "voice", "stage", "movie",
    "actor", "scone", "right", "story", "novel",
    "write", "speak", "learn", "study", "think",
    "solve", "build", "craft", "shape", "model",
    "earth", "ocean", "river", "mount", "field",
    "proud", "funky", "trail", "cleft", "slope",
    "storm", "windy", "frost", "humid", "fresh",
    "night", "daunt", "dusky", "solar", "lunar"
]

#choose_word() - Selects a random word

def choose_word():
    secret_word = random.choice(words)
    return secret_word

#get_guess() – Gets and validates the player’s guess.

def get_guess(previous_guesses):
    while True:
        player_guess = str(input("Make a guess: ")).lower().strip()

        if len(player_guess) != 5 or not player_guess.isalpha():
            print("Invalid input. Please enter a 5 letter word.")
        elif player_guess in previous_guesses:
            print("You have already guessed this word! Try again.")

        else:
            previous_guesses.append(player_guess)
            return player_guess

#evaluate_guess() – Compares the guess with the secret word and returns feedback.
 
def evaluate_guess(secret_word, player_guess):
    feedback = []
    for i in range(5):
        if player_guess[i] == secret_word[i]:
            feedback.append("G")
        elif player_guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback

#display_guess() – Displays the guess and its feedback.

def display_guess(feedback, player_guess):
    print(" ".join(player_guess))
    print(" ".join(feedback))

#has_won() – Determines whether the player has guessed the word.

def has_won(player_guess, secret_word):
    return player_guess == secret_word