import os
from art import logo
print(logo)
def highest_bid(bid_record):
    high_bid=0
    winner=""
    for bidder in bid_record:
        bid_price=bid_record[bidder]
        if bid_price>high_bid:
            high_bid=bid_price
            winner=bidder
    print(f"The winner is {winner} with ${high_bid} bid")
    
bid={}
finish=False
# asking for name and bid 
while not finish:
    name=input("What is your name ? : ")
    price=int(input("What is your bid? : $"))
    bid[name]=price
    should_continue=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue=="no":
        finish=True
        highest_bid(bid)
    elif should_continue=="yes":
        os.system('clear')
        
        
enteries=input("Do you want to check all entries Type 'yes' or 'no' :")
if enteries=="yes":
    for bidder in bid:
        print(f"Name : {bidder}, Bid Price :${bid[bidder]}")
else:
    print("Exit")