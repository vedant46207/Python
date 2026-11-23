import sys

def display(iNo1, iNo2):
    print(iNo1*iNo2)


def main():
    iValue1 = 0
    iValue2 = 0

    try :
        iValue1 = int(input("Enter length: "))
        iValue2 = int(input("Enter width: "))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2)

if __name__ == "__main__": main()
"""
Enter length: 2
Enter width: 3
6
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % python3 a10_2.py
Enter length: 4
Enter width: 5
20
"""
