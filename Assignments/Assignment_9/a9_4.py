import sys

def display(iNo):

    if iNo<0 : iNo = -iNo
    iMul = 1 

    for i in range (1, iNo+1 ):
        if(i%2 != 0) :
            iMul = iMul * i

    print(iMul )

def main():
    iValue = 0 

    try :
        iValue = int(input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter number :5
15
vedantbarne@Vedants-MacBook-Air-2 Assignment_9 % python3 a9_4.py
Enter number :-5
15
vedantbarne@Vedants-MacBook-Air-2 Assignment_9 % python3 a9_4.py
Enter number :10
945      	
"""

