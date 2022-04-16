#calculator using list and dictionaries
import os
from art import logo

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def Calculator():
    print(logo)
    
    num1=float(input("Enter first numer :"))
    should_continue=True
    while should_continue:
        num2=float(input("Enter next number : "))
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick up operation form above line : ")
        cal_func=operations[operation_symbol]
        answer=cal_func(num1,num2)
        print(f"{num1} {operation_symbol} {num2} ={answer}")
        
        if input("Type 'y' for continue calculating or 'n' for exit : ").lower()=="y":
            num1=answer
            num3=num2
        else:
            should_continue=False
            os.system('clear')
            Calculator()

Calculator()
    
