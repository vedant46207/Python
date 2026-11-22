import sys

def display(iNo):
    if iNo<0 : iNo = -iNo
    for i in range (1, 1+iNo):
        if i%2 != 0 : print(i, end = "\t")

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
Enter a number :18
1	3	5	7	9	11	13	15	17	
vedantbarne@Vedants-MacBook-Air-2 Assignment_7 % python3 a7_4.py
Enter a number :14
1	3	5	7	9	11	13	
"""

