import sys

def display(iNo1, iNo2):
    if iNo1> 60 and iNo2 >17 :return True
    else: return False

def main():

    iValue1 = 0 
    iValue2 = 0 
    bRet = False 

    try :
        iValue1 = int(input ("Enter marks :"))
        iValue2 = int(input("Enter age :"))

    except ValueError :
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    bRet = display(iValue1, iValue2 )
    if (bRet == True) : print("Eligible")
    else : print("Not eligible")

if __name__ == "__main__": main()

"""
Enter marks :75
Enter age :19
Eligible
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_1.py
Enter marks :90
Enter age :17
Not eligible
"""