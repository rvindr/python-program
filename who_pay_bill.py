print('Welcome to the who paid the bill Game')
import random
from unicodedata import name
# input for all names for billing
names=input("Write all names split with commans\n")
# converting input into lists 
names_as_lists=names.split(",")
print(f"Names for billing :{names_as_lists}")
# name_len=len(names_as_lists)
# rand=random.randint(0,name_len-1)
# print(f"Bill paid by {names_as_lists[rand]}")
name_of_person=random.choice(names_as_lists)
print(f"{name_of_person} pay bill")



# in this program use=> random.randint or random.choice()