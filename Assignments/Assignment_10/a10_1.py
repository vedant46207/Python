import sys

def display(iNo):
    print(3.14*iNo*iNo)


def main():
    iValue = 0.0

    try :
        iValue = float(input("Enter radius: "))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()
"""
Enter radius: 5.3
88.20259999999999
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % python3 a10_1.py
Enter radius: 10.4
339.6224000000001
"""
