import sys

def display(iNo):
    print("in m :", iNo*1000)


def main():
    iValue = 0

    try :
        iValue = int(input("Enter in km: "))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()
"""
Enter in km: 5
in m : 5000
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % python3 a10_3.py
Enter in km: 4
in m : 4000
vedantbarne@Vedants-MacBook-Air-2 Assignment_10 % python3 a10_3.py
Enter in km: 6
in m : 6000
"""
