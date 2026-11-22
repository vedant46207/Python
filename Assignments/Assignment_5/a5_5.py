import sys

def checkCharacterType(cValue):
    if(cValue >= 'A' and cValue <= 'Z'):print("Uppercase Alphabet")
    elif(cValue >= 'a' and cValue <= 'z'):print("Lowercase Alphabet")
    elif(cValue >= '0' and cValue <= '9'):print("Digit")
    else : print("Special Character")


def main():
    cValue = ""

    cValue = input("Enter a character :")

    if(len(cValue) != 1):
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    checkCharacterType(cValue)

if __name__ == "__main__": main()

"""
Enter a character :A
Uppercase Alphabet
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_5.py
Enter a character :m
Lowercase Alphabet
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_5.py
Enter a character :7
Digit
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_5.py
Enter a character :@
Special Character
"""