"""
function name : divice 
description: divides two numbers 
input : two integers 
output : division result 
author :Vedant Kalidas Barne
date : 20/11/2026
"""
def Divide (iNo1 , iNo2 ):
    iAns = 0 
    if(iNo2 == 0):return None
    iAns = int(iNo1/iNo2)
    return iAns 

    
def main():
    iValue1 = 0 ;
    iValue2 = 0 ;
    iRet = 0 ;
    print("Enter first number :", end ="")
    try:
        iValue1 = int(input ())
    except ValueError:
        print("Invalid input")
        return 1 
    print("Enter second number :", end = "")
    try :
        iValue2 = int(input())
    except ValueError:
        print("Invalid input")
        return 1 
    iRet = Divide(iValue1,iValue2)

    if (iRet is None): print("Division by zero is not possible")
    else : print("Division is : ", iRet )

    return 0 

if __name__ == "__main__":
    main()

"""
Enter first number :5
Enter second number :5
Division is :  1
vedantbarne@Vedants-MacBook-Air-2 Assignment_1 % python3 a1_1.py
Enter first number :10
Enter second number :5
Division is :  2
vedantbarne@Vedants-MacBook-Air-2 Assignment_1 % python3 a1_1.py
Enter first number :16
Enter second number :2
Division is :  8
"""

