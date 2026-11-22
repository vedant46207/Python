import sys

def display(iNo):
    if iNo<0 : iNo = -iNo
    for i in range (1, 1+iNo):
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
Enter a number :8
1	2	3	4	5	6	7	8	
vedantbarne@Vedants-MacBook-Air-2 Assignment_7 % python3 a7_2.py
Enter a number :5
1	2	3	4	5	
vedantbarne@Vedants-MacBook-Air-2 Assignment_7 % python3 a7_2.py
Enter a number :4
1	2	3	4
"""

