import random
print("Welcome to Rock Paper Scissor game")
rock='''

██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
'''
paper='''

██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
'''
scissor='''

░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝

'''

# listing images 
image=[rock,paper,scissor]

# function for result
def game(comp,user):
    # if both have same choice 
    if comp==user:
        return None
    
    # if computer choose rock
    if comp==1:
        if user==2:
            return True
        elif user==3:
            return False
    # if computer choose paper
    if comp==2:
        if user==3:
            return True
        elif user==1:
            return False
        
    # if computer choose scissor
    if comp==3:
        if user=="2":
            return False
        elif user=="1":
            return True


# getting input from user and computer
user=int(input('Type "1" for Rock, "2" for paper, "3" for scissor\n'))
print(f"You choose :")
print(image[user-1])

comp=random.randint(1,3)
print("computer choose :")
print(image[comp-1])





result=game(comp,user)

if result==None:
    print("Game Draw")
elif result==True:
    print("You win!")
elif result==False:
    print("You loose! Try next time")