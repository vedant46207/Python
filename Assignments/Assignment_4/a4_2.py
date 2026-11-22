import sys

def display(iNo):
    if iNo %2 ==0 : print("EVEN")
    else : print("ODD")
    print()

def main():
    iValue = 0 

    try : 
        iValue = int(input("Enter a number :"))
    except ValueError :
        print("Invalid input " , file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__" : main()
"""
Enter a number :8
EVEN

vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_2.py
Enter a number :5
ODD
"""
