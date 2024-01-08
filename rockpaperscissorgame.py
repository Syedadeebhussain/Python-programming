import random
users_choice=int(input("enter 0 for rock,1 for paper,2 for scissor"))
if users_choice>=0 and users_choice<=2:
    computer_choice=random.randint(0,2)
    if users_choice==computer_choice:
        print("IT'S A DRAW")
    elif users_choice==2 and computer_choice==0:
        print("COMPUTER WINS AMD YOU LOOSE")
    elif users_choice==0 and computer_choice==2:
        print("YOU WINS AMD COMPUTER LOOSE")
    elif users_choice>computer_choice:
        print("YOU WINS AMD COMPUTER LOOSE")
    else:
        print("COMPUTER WINS AMD YOU LOOSE")
else:
    print("Wrong input")