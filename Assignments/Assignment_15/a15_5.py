import sys

def percentage(iTotal, iObtained):
    if(iTotal == 0): return 0.0
    return (iObtained / iTotal) * 100

def main():
    iValue1 = 0
    iValue2 = 0
    fRet = 0.0

    try :
        iValue1 = int(input("Please enter total marks :"))
        iValue2 = int(input("Please enter obtained marks :"))
    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    if(iValue1 <= 0 or iValue2 < 0 or iValue2 > iValue1):
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    fRet = percentage(iValue1, iValue2)
    print(f"Percentage is {fRet}%")

if __name__ == "__main__": main()

"""
Please enter total marks :1000
Please enter obtained marks :745
Percentage is 74.5%
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_5.py
Please enter total marks :0
Please enter obtained marks :10
Invalid input
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % 
"""