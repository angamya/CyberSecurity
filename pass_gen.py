# password generator
import random
import string

def generate_password(min_Length, numbers=True, special_charakters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    charakters=letters
# += to add a value to an existing variable and assign the new value back to the same variable.  
    if numbers:
        charakters += digits
    if special_charakters: 
        charakters += special
    pwd =''
    meets_criteria =False
    has_number = False
    has_special = False
# jeśli jedno z załozen jest True to kontynuuj
    while not meets_criteria or len(pwd) < min_Length:

     new_char = random.choice(charakters)
     pwd += new_char
     if new_char in digits:   
        has_number=True
     elif new_char in special:   
        has_special=True

    # if true/false
     meets_ctiteria =True
     if numbers:
         meets_criteria = has_number
     if special_charakters:
         meets_criteria = meets_criteria and has_special

    return pwd


min_Length= int(input("Enter your minimum length: "))
has_number= input("Do you want to have numbers y/n? ").lower() =="y"
has_special= input("Do you want to have special characters y/n? ").lower() =="y"
pwd = generate_password(min_Length,has_number, has_special)
print("The genereted password is: ",pwd)
