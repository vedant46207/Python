import sys

def display(iNo):
    for i in range (1, 6):
        print(i*iNo, end ="\t")

    print()

def main():
    iValue = 0 

    try : iValue = int(input("Enter a number :"))
    except ValueError : 
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter a number :4
4	8	12	16	20	
vedantbarne@Vedants-MacBook-Air-2 Assignment_7 % python3 a7_5.py
Enter a number :7
7	14	21	28	35
"""

