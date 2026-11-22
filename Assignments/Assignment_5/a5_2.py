import sys

def checkLeapYear(iYear):
    if(iYear <= 0):print("Invalid Year")
    elif((iYear % 400 == 0) or (iYear % 4 == 0 and iYear % 100 != 0)):print("Leap Year")
    else : print("Not a Leap Year")


def main():
    iYear = 0

    try : 
        iYear = int(input("Enter year :"))

    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    checkLeapYear(iYear)

if __name__ == "__main__": main()

"""
Enter year :2024
Leap Year
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_2.py
Enter year :1900
Not a Leap Year
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_2.py
Enter year :2000
Leap Year
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_2.py
Enter year :0
Invalid Year
"""