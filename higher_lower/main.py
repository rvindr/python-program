from traceback import print_tb
from art import logo,vs
from game_data import data
import random
import os

def format_data(account):
    account_name=account['name']
    account_desc=account['description']
    account_country=account['country']
    return f"{account_name},a {account_desc}, from {account_country}"

def check_guess(guess,account_a_count,account_b_count):
    if account_a_count>account_b_count:
        return guess=='a'
    else:
        return guess=='b'  
    
account_b=random.choice(data)

#print logo
print(logo)
score=0
should_continue=True
while should_continue:
    #generate two random account
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
        
    print(f"Compare : {format_data(account_a)}")
    print(vs)
    print(f"Against : {format_data(account_b)}")

    # taking input from usr 
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    os.system('clear')
    print(logo)
    

    account_a_count=account_a['follower_count']
    account_b_count=account_b['follower_count']

    is_correct=check_guess(guess,account_a_count,account_b_count)
    if is_correct:
        score+=1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue=False
        