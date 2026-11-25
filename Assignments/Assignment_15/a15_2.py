import sys

def chkGreater(iNo):
    if(iNo > 100): return True
    else : return False

def main():
    iValue = 0
    bRet = False

    try :
        iValue = int(input("Please enter number :"))
    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    bRet = chkGreater(iValue)
    if(bRet): print("Greater")
    else : print("Smaller")

if __name__ == "__main__": main()

"""
Please enter number :101
Greater
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_2.py
Please enter number :39
Smaller
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % python3 a15_2.py
Please enter number :abc
Invalid input
vedantbarne@Vedants-MacBook-Air-2 Assignment_15 % 
"""