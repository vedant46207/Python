import sys

def chkEqual(iNo1, iNo2):
    if(iNo1 == iNo2): return True
    else : return False

def main():
    iValue1 = 0
    iValue2 = 0
    bRet = False

    try :
        iValue1 = int(input("Enter first number :"))
        iValue2 = int(input("Enter second number :"))
    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    bRet = chkEqual(iValue1, iValue2)
    if(bRet): print("Equal")
    else : print("Not Equal")

if __name__ == "__main__": main()

"""
Enter first number :10
Enter second number :10
Equal
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_3.py
Enter first number :10
Enter second number :12
Not Equal
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_3.py
Enter first number :10
Enter second number :-10
Not Equal
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % 
"""