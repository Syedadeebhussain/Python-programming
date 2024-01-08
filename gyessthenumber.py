import random
easy_level_attempts=10
hard_level_attempts=5
def choose_level(level):
    if level=="hard":
        return hard_level_attempts
    elif level=="easy":
        return easy_level_attempts
    else:
        print("YOU HAVE CHIISEN WRONG LEVEL")
        return 0
def guessed_numberfunction(guess_number,computer_choice,attempts):
    if guess_number>computer_choice:
        print(f"YOUR GUESS IS TO HIGH")
        return attempts-1
    elif guess_number<computer_choice:
        print(f"YOUR GUESS IS TO LOW")
        return attempts-1
    else:
        print(f"YOUR GUESS IS RIGHT.....THE CORRECT ANSWER IS {computer_choice}")
def game():
    print("LET ME THINK OF A NUMBER")
    computer_choice=random.randint(1,50)
    level=input("CHOOSE LEVEL OF DIFFICULTY")
    attempts=choose_level(level)
    guess_number=0
    while guess_number!=computer_choice:
       print(f"you have {attempts} remaining to guess a number")
       guess_number=int(input("GUESS A NUMBER"))
       attempts=guessed_numberfunction(guess_number,computer_choice,attempts)
    if attempts==0:
        print("YOU ARE OUT OF GUESS.....YOU LOOSE")
    elif guess_number!=computer_choice:
        print("f{guess_number}")
game()    