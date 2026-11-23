import sys

def display(iNo):
    print((iNo-32)*(5/9))


def main():
    iValue = 0.0

    try :
        iValue = float(input("Enter F: "))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()
"""
Enter F: 10
-12.222222222222223
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % 
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % python3 a10_4.py
Enter F: 34
1.1111111111111112
"""
