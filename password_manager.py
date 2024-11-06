import hashlib
import getpass

password_manager={}

def create_account():
    username=input("Enter your username: ")
    password=getpass.getpass("Enter your password: ")
    hashedpaswd= hashlib.sha256(password.encode()).hexdigest()
    password_manager[username]=hashedpaswd
    print("Account created!")

def login():
    username=input("Enter your username: ")
    password=getpass.getpass("Enter your password: ")
    hashedpaswd= hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username]==hashedpaswd:
     print("---login succesful---")
    else:
       print("Invalid username or password.")

def main():
    while True:
        choice=input("Enter  \n -1- to create account \n -2- to login \n -3- to exit \n: ")
        if choice == '1':
         create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
      




