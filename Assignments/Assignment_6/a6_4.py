import sys

def display(iNo1, iNo2, iNo3):
    if(
        iNo1+iNo2 == iNo3 
        or
        iNo2+iNo3 == iNo1
        or 
        iNo3+iNo1 == iNo2
        ): return True 
    else : return False 

def main():

    iValue1 = 0 
    iValue2 = 0 
    iValue3 = 0 
    bRet = False 

    try :
        iValue1 = int(input ("Enter first side :"))
        iValue2 = int(input("Enter second side  :"))
        iValue3 = int(input ("Enter third side :"))

    except ValueError :
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    bRet = display(iValue1, iValue2,iValue3 )
    if (bRet == True) : print("Valid Triangle")
    else : print("Not a triangle")

if __name__ == "__main__": main()

"""
Enter first side :3
Enter second side  :4
Enter third side :7
Valid Triangle
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_4.py
Enter first side :5
Enter second side  :1
Enter third side :6
Valid Triangle
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_4.py
Enter first side :3
Enter second side  :4
Enter third side :5
Not a triangle
"""