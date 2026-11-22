import sys

def display(iNo):
    if iNo >= 18 : print("eligible")
    else : print("not eligible")


def main():
    iValue = 0 

    try : 
        iValue = int(input("Enter age :"))
    except ValueError :
        print("Invalid input " , file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__" : main()
"""
Enter age :18
eligible
vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_4.py
Enter age :19
eligible
vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_4.py
Enter age :16
not eligible
"""
