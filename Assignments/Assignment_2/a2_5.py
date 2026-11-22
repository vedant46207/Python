
import sys
def evenodd(iNo):
    return iNo%2 == 0 
def main():
    iValue = 0 
    bRet = False

    try : iValue = int(input("Enter a number :"))
    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    bRet = evenodd(iValue)
    if bRet == True : print("EVEN")
    else : print("ODD")

if __name__ == "__main__":
    main()


"""
Enter a number :4
EVEN
vedantbarne@Vedants-MacBook-Air-2 Assignment_2 % python3 a2_5.py
Enter a number :9
ODD
vedantbarne@Vedants-MacBook-Air-2 Assignment_2 % python3 a2_5.py
Enter a number :12
EVEN
"""