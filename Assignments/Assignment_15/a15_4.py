import sys

def multiply(iNo1, iNo2, iNo3):
    iMul = 1

    if(iNo1 == 0 and iNo2 == 0 and iNo3 == 0): return 0

    if(iNo1 != 0): iMul = iMul * iNo1
    if(iNo2 != 0): iMul = iMul * iNo2
    if(iNo3 != 0): iMul = iMul * iNo3

    return iMul

def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    iRet = 0

    try :
        iValue1 = int(input("Enter first number :"))
        iValue2 = int(input("Enter second number :"))
        iValue3 = int(input("Enter third number :"))
    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    iRet = multiply(iValue1, iValue2, iValue3)
    print("Multiplication is", iRet)

if __name__ == "__main__": main()

"""
Enter first number :5
Enter second number :4
Enter third number :7
Multiplication is 140
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_4.py
Enter first number :5
Enter second number :0
Enter third number :7
Multiplication is 35
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_4.py
Enter first number :5
Enter second number :0
Enter third number :0
Multiplication is 5
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_4.py
Enter first number :0
Enter second number :0
Enter third number :0
Multiplication is 0
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % 
"""