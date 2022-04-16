from dis import dis
from operator import imod
import random
# import hangman_art
from hangman_art import *
from hangman_word import *
print(logo)
chosen_word=random.choice(word_list)
# testing code 
print(f"The solution is {chosen_word}")
word_len=len(chosen_word)
lives=6
end_of_game=False
 # display _ according to character
display=[]
for _ in range(word_len):
    display+="_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess=input("Enter Guess: ").lower()
   
    if guess in display:
      print(f"You've already guessed {guess}")       
      
    # replacing _ with letter 
    for position in range(word_len):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=letter
    print(f"{' '.join(display)}")      
         
    if guess not in chosen_word:
            print(f"You guess {guess}, that's not in the word. You lose a life")
            lives-=1
            if lives==0:
                end_of_game=True
                print("You lose the game")
    if "_" not in display:
            end_of_game=True
            print("You win")
    print(stages[lives])
    print(f"Lives remaining {lives}")
    