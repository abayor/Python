import random
from guesslogo import art
print (art)
easy_trial = 10
hard_trial = 5

'''print("I'm thinking of a number between 1 and 100")
number = int(random.randint(1, 100))
guess = int(input("Guess the Number:"))
con_guess = int(guess)
'''

def check_guess(guess, number, lev_e):
    if guess > number:
        print("Too High")
        return lev_e - 1 
    elif guess < number:
        print("too low")
        return lev_e - 1 
    else:
        print("Correct !!, You guessed Right Number is {0}" .format(number))
        
def set_difficilty():
    dif = (input("Choose a Difficulty \n \n Type \'easy' or e for Easy Level \n\n Type \'hard' or h for Hard Level\n\n Difficulty:")).lower()
    if dif == 'easy' or dif == 'e':
        return easy_trial
    elif dif == 'hard' or dif == 'h':
        return  hard_trial
    else:
        inva = print("invalid input type 'hard' or 'easy")
        return inva
def play():

    print("Welcome to Number Guess Game")
    print("I'm thinking of a number between 1 and 100")
    lev_e = set_difficilty() 
    number = random.randint(1, 100)
    guess = int(input("Guess the Number:"))
    #con_guess = int(guess)
    while guess != number:
        print("Make another Guess, You have {} trials left:".format(lev_e))
        guess =int(int(input("Guess the Number:")))
        lev_e = check_guess(guess, number, lev_e)
        if lev_e == 0:
            print("Game Over you loss")
            return
        elif guess!= number:
            print("Wrong!")
    
     
    #print("You have {0} attempt left".format(lev_e)
    
    
play()

 