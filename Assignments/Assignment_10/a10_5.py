import sys

def display(iNo):
    print(iNo*0.0929)


def main():
    iValue = 0.0

    try :
        iValue = float(input("Enter number: "))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()
"""
Enter number: 5
0.46449999999999997
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % python3 a10_5.py
Enter number: 7
0.6503
"""
