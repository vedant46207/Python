import sys 
import re 

def displayName (sName ) :
    print("Entered name is :", sName)

def main():
    sName = ""

    sName = input("Enter a name :")
    if(sName.strip() == "" or not re.fullmatch(r"[A-Za-z ]+", sName)):
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    displayName(sName)

if __name__ == "__main__": main()
"""
Enter a name :Vedant Barne
Entered name is : Vedant Barne
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_1.py
Enter a name :marvellous
Entered name is : marvellous
"""