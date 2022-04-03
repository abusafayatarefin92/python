i = 1

while i <= 10:
    print(i)
    i += 1

print("Done with loop")

secret_animal = "giraffe"
guess = ""
out_of_guesses = False
guess_count = 0
guess_limit = 3

while guess != secret_animal and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Insert the animal name: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses! you lose")
else:
    print("You win")

