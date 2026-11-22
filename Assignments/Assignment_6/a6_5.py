import sys

def display(iNo1, iNo2):
    if iNo2 >10 : print("Bonous :",0.15*iNo1) 
    elif(iNo2>5 and iNo2<= 10):print("Bonous :",0.1*iNo1)
    elif(iNo2<=5):print("Bonous :",0.05*iNo1)

def main():

    iValue1 = 0 
    iValue2 = 0 
    bRet = False 

    try :
        iValue1 = int(input ("Enter monthly salary :"))
        iValue2 = int(input("Enter years working :"))

    except ValueError :
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2 )

if __name__ == "__main__": main()

"""
Enter monthly salary :30000
Enter years working :12
Bonous : 4500.0
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_5.py
Enter monthly salary :20000
Enter years working :7
Bonous : 2000.0
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_5.py
Enter monthly salary :10000
Enter years working :2
Bonous : 500.0
"""