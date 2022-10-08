
import random
guess=1
def program():
    guess = 1
    print("select any one option of range in which you want that the computer will select any random no for you:-\n"
          "1 - Range Between 1 to 10\n"
          "2 - Range Between 1 to 100\n"
          "3 - for Any Range")
    option = int(input("select any one option from the above three Options :- "))
    if (option == 1):
        guess = 1
        numbers = int(input("enter the number you guess that the computer is selected for you,you have only 10 chances:- "))
        a = random.randint(1, 10)
        while(True):
            if (numbers == a):
                print("you make a correct choice")
                break
            else:
                print("this is not the correct choice")
                break
            print(10 - guess, "No of guesses left")
            guess = guess + 1
        if(guess>=10):
            print("you have no chances left")


    elif (option == 2):
        numbers = int(input("enter the number you guess that the computer is selected for you,you have only 10 chances:- "))
        b = random.randint(1, 100)
        if (numbers == b):
            print("you make a correct choice")
        else:
            print("this is not the correct choice")
    elif (option == 3):
        numbers = int(input("enter the number you guess that the computer is selected for you,you have only 10 chances:- "))
        c = random.randint(1, 100)
        if (numbers == c):
            print("you make a correct choice")
        else:
            print("this is not the correct choice")
    else:
        print("please select an one option from the given three options\n")
        program()

program()
"""
def main():
    numbers = int(input("enter the number you guess that the computer is selected for you:- "))

main()
"""