import random
from traceback import print_tb
from art import logo

def guess_check(guess):
    ''' This function take one guess number and check guessed number is right ,too high or too low'''
    if guess==chosen_num:
        print(f"You got it! The answer was {chosen_num}.")
        return True
    elif guess>chosen_num:
        print("Guess Too High")
    elif guess<chosen_num:
        print("Guess Too Low")
        
    
    
chosen_num=random.randint(1,101)
# testing code 
print(f"The solution is : {chosen_num}")

# while loop if user type invalid input 
invalid=False
while not invalid:
    level=input("Choose a Difficulty level, Type 'easy' or 'hard' : ").lower()
    
    
    if level=="easy":
        attempt=10
        invalid=True
    elif level=="hard":
        attempt=5
        invalid=True
    else:
        print("Invalid input, Try Again!")
        invalid=False
print(f"You have {attempt} attemp for guess the number")    
guess=int(input("Make a guess : "))

result=guess_check(guess)
while not result :
    attempt-=1
    print(f"You have {attempt} attempt remaining to guess the number")
    guess=int(input("Make another guess : "))
    # calling function 
    result=guess_check(guess)
     
    
    if attempt==0:
        print("You don't have remaining life\n You Loose the game")
        result=True
    
    

