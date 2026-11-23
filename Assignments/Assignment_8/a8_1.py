import sys

def display(iNo):
    if(iNo<50): print("Small")
    elif(iNo >=50 and iNo <100):print("Medium")
    elif(iNo >100) : print("Large")


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
Enter number :80
Medium
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_1.py
Enter number :30
Small
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_1.py
Enter number :110
Large
"""

