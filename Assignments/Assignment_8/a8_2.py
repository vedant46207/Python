import sys

def display(iNo):
    if(iNo == 1) : print("One")
    elif iNo == 2 : print("Two")
    elif iNo == 3 : print("Three")
    elif iNo == 4 : print("Four")
    elif iNo == 5 : print("Five")
    elif iNo == 6 : print("Six")
    elif iNo == 7 : print("Seven")
    elif iNo == 8 : print("Eight")
    elif iNo == 9 : print("Nine")
    else : print("Invalid input")


def main():
    iValue = 0 

    try :
        iValue = int(input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter number :2
Two
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_2.py
Enter number :6
Six
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_2.py
Enter number :9
Nine
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_2.py
Enter number :12
Invalid input
"""

