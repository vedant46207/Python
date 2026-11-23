import sys

def display(iNo):
    print(70*iNo)


def main():
    iValue = 0 

    try :
        iValue = int(input("Enter in dollar :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter in dollar :1
70
vedantbarne@Vedants-MacBook-Air-2 Assignment_9 % python3 a9_2.py
Enter in dollar :3
210
vedantbarne@Vedants-MacBook-Air-2 Assignment_9 % python3 a9_2.py
Enter in dollar :1200
84000        	
"""

