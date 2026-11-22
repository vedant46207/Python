import sys

def display(iNo):
    if iNo %5 ==0 : print("Divisible by 5")
    else : print("Not divisible by 5")
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
Enter a number :15
Divisible by 5

vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_5.py
Enter a number :45
Divisible by 5

vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_5.py
Enter a number :59
Not divisible by 5
"""
