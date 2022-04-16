# adding even number 1 to 100

from traceback import print_tb


total=0
for number in range(1,101):
    if(number%2==0):
     total+=number
print(total)

tot=0
for number in range(2,101,2):
    tot+=number
print(tot)