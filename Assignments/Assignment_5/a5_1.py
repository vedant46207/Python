import sys

def findGreatest(iFirst, iSecond, iThird):
    if(iFirst >= iSecond and iFirst >= iThird):print(iFirst, "is Greatest")
    elif(iSecond >= iFirst and iSecond >= iThird):print(iSecond, "is Greatest")
    else : print(iThird, "is Greatest")


def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0

    try : 
        iValue1 = int(input("Enter first number :"))
        iValue2 = int(input("Enter second number :"))
        iValue3 = int(input("Enter third number :"))

    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    findGreatest(iValue1, iValue2, iValue3)

if __name__ == "__main__": main()

"""
Enter first number :10
Enter second number :50
Enter third number :30
50 is Greatest
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_1.py
Enter first number :40
Enter second number :40
Enter third number :20
40 is Greatest
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_1.py
Enter first number :15
Enter second number :15
Enter third number :15
15 is Greatest
"""