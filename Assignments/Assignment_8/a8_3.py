import sys

def display(iNo):
    iMul = 1 
    if iNo<0 : iNo = -iNo

    for i in range (1 , iNo+1 ):
        iMul = iMul*i 

    return iMul



def main():
    iValue = 0 
    iRet = 0

    try :
        iValue = int(input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    iRet = display(iValue)
    print(iRet)

if __name__ == "__main__": main()

"""
Enter number :5
120
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_3.py
Enter number :-5
120
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_3.py
Enter number :4
24
"""

