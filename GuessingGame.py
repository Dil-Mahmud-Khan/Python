# Guess Game
secret_word = "Elephant"
guess = ""
guess_count = 0
guess_limit = 3
out_off_guesses = False
while guess != secret_word and not (out_off_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the word: ")
        guess_count += 1
    else:
        out_off_guesses = True
if out_off_guesses:
    print("You LOSE!")
else:
    print("You Win")
