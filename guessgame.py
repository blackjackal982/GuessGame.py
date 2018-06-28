
import random
def play():
    print("Welcome to the Guess Game!!")
    print("Let the PC guess a number!")
    target_number = random.randint(1,100)
    guesslist=[]
    res = 1
    count = 0
    while res == 1 or res == -1:
        try:
            guessnumber=int(input("Guess a number between 1 - 100:\n"))
            if guessnumber<0 or guessnumber >100:
                raise TypeError("Invalid guess")
            res = check(guessnumber, target_number)
            guesslist.append(guessnumber)
        except TypeError as te:
            raise TypeError("Invalid number entered .Try again")
            continue


    print("Game Summary:")
    print("You took {0} attempts".format(len(guesslist)))
    for i in guesslist:
        if i < target_number:
            print("Your {0} guess was {1} which was lower than {2}".format(guesslist.index(i),i,target_number))
        elif i > target_number:
            print("Your {0} guess was {1} which was higher than {2}".format(guesslist.index(i), i, target_number))
        elif i == target_number:
            print("Your {0} guess was {1} which was the correct number".format(guesslist.index(i), i))

def check(guessnumber,target_number):
    if guessnumber < target_number:
        #guessed number is less than actual number return -1
        print("Guess lower")
        return -1
    elif guessnumber > target_number:
        #guessed number is higher than actual number return 1
        print("Guess higher")
        return 1
    elif guessnumber == target_number:
        print("You are rightt")
        return 0

play()
