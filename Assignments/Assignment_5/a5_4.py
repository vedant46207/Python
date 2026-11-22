import sys

def checkMultipleDivisibility(iValue):
    if(iValue % 3 == 0 and iValue % 5 == 0):print("Divisible by Both")
    elif(iValue % 3 == 0):print("Divisible by 3 Only")
    elif(iValue % 5 == 0):print("Divisible by 5 Only")
    else : print("Not Divisible by Either")


def main():
    iValue = 0

    try : 
        iValue = int(input("Enter number :"))

    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    checkMultipleDivisibility(iValue)

if __name__ == "__main__": main()

"""
Enter number :15
Divisible by Both
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_4.py
Enter number :9
Divisible by 3 Only
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_4.py
Enter number :10
Divisible by 5 Only
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_4.py
Enter number :7
Not Divisible by Either
"""