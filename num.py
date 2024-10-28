import random

def number_guessing_game():

    try:
        randomNumber= random.randint(1,100)
        attempt= 0


        while True:
            gauss = int(input('Input your gauss number: '))
            attempt += 1

            if randomNumber > gauss:
                print('Too Low')
            elif gauss > randomNumber:
                print("Too High")
            else:
                print(f"Congratulations! You've guessed the number in {attempt} attempts.")
                break

    except ValueError:
        print("Invalid input! Please enter a valid number.")


number_guessing_game()

