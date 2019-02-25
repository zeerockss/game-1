import random
import time
def guessing_num():
    name = input("Please mention your name:").upper()
    print("Hello ",name," Let's Play the Game!!")
    our_num = [528, 435, 567,789,600]
    correct_num = random.choice(our_num)
    guess_num = int()
    guess_count = 0
    guess_limit = 5
    out_of_guess_limit = False
    while guess_num != correct_num and not (out_of_guess_limit):
        guess_num = int(input("Enter your guess number:"))
        guess_count += 1
        if guess_num == correct_num:
            print("Congrats!!",name," You Guessed it correct in ",guess_count, " attempt.")
        elif guess_count == guess_limit:
            print("Sorry! The maximum limit for guessing is only 5 Times")
            time.sleep(2)
            print(name,"you lose the game.The Correct number was ",correct_num)
            out_of_guess_limit = True
        else:
            print("Wrong Guess!!Try Again")



def main():
    choice = "y"
    while choice == "y":
        guessing_num()
        time.sleep(2)
        choice = input("Play again? Enter 'y' if YES and 'n' if NOT(y/n) : ").lower()
        if choice == "n":
            print("Bye!!")


if __name__ == '__main__':
    main()
