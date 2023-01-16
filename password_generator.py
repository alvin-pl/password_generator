# Password Generator

"""
STEPS
1. Get the numbers, symbols, letters
2. Enter a password 
3. If password length is equal to itself, replace it with a random letter, number, or symbol
"""
from random import sample

letr_nums_symb = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "!", "@", "#", "$", "%", "^", "&", "*", ".", "?"]

    
def input_text():
    password = input("Enter username: ")
    return password  
#how to transfer values to another function
passwordOutput = input_text()


def generate_new_pw():
    if passwordOutput == passwordOutput:
        #print("Old password: " + passwordOutput)
        #chooses 12 random values from a list 
        print("Here's your generated password:", sample(letr_nums_symb, 12))
generate_new_pw()
    
    