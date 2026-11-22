import sys

def display(iNo):
    if iNo<0 : iNo = -iNo
    for i in range (-iNo, 1+iNo):
        print(i, end = "\t")

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
-4	-3	-2	-1	0	1	2	3	4	
vedantbarne@Vedants-MacBook-Air-2 Assignment_7 % python3 a7_3.py
Enter a number :5
-5	-4	-3	-2	-1	0	1	2	3	4	5	
"""

