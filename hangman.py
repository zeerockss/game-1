import random
word_list = ["python", "java", "android"]
our_word = random.choice(word_list)
guessed_letters = []
guess_word = ""
def display_word():
    word = ""
    for letter in our_word:
        if letter in guessed_letters:
            print(letter ,"", end="")
            word += letter
        else:
            print("_ ",end="")
    return word
def check_word():
    win = False
    attempts = 7
    while attempts > 0 and not win:
        guess_word = display_word()
        if guess_word != our_word and not win:
            guess = input("Please choose a word:").lower()
            guessed_letters.append(guess)
            print("guessed_letteres:", guessed_letters)
            if len(guess) > 1:
                print("Sorry !! You Entered more than one character.")
            elif not guess.isalpha():
                print("Enter a letter between(A-Z")
            elif guessed_letters.count(guess)>1:
                    print("You already guessed it")
            if not guess in our_word :
                print("wrong guess")
                attempts -= 1
                print("you have", attempts, " attempts remaining")
            if attempts == 6:
                print(" o ")
                print(" | ")

            elif attempts == 5:
                print(" o ")
                print(" | ")
                print("/ ")

            elif attempts == 4:
                print(" o ")
                print(" | ")
                print("/ \  ")

            elif attempts == 3:
                print(" o ")
                print(" | ")
                print("/ \ ")
                print(" |")

            elif attempts == 2:
                print(" o ")
                print(" | ")
                print("/ \ ")
                print(" |")
                print("/  ")
            elif attempts == 1:
                print(" o ")
                print(" | ")
                print("/ \ ")
                print(" |")
                print("/ \ ")
            elif attempts == 0:
                print("Sorry the game is over !! You Lose. The Word was", our_word)
        else:
            win = True
            print()
            print("Congrats you guessed the world! You Win")

check_word()