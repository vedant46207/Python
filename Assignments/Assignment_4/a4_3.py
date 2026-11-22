import sys

def display(iNo1, iNo2):
    if(iNo1 > iNo2 ): print(iNo1 ," is greater than ",iNo2)
    elif(iNo1== iNo2): print("Equal numbers")
    else: print(iNo2 , " is greater than ",iNo1)


def main():
    iValue1 = 0 
    iValue2 = 0 

    try : 
        iValue1 = int(input("Enter first number :"))
        iValue2 = int(input("Enter second number"))
    except ValueError :
        print("Invalid input " , file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2)

if __name__ == "__main__" : main()
"""
Enter first number :4
Enter second number5
5  is greater than  4
vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_3.py
Enter first number :8
Enter second number3
8  is greater than  3
vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_3.py
Enter first number :3 
Enter second number8
8  is greater than  3
"""
