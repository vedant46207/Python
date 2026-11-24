import sys

def display(iNo):
    i = 0 
    ieven = 0 
    iodd = 0 
    isum = 0 

    if iNo<0: iNo = -iNo
    if iNo ==0 : print(iNo)

    while iNo!=0 :
        i = iNo%10
        if(i%2==0): ieven = ieven +i 
        else : iodd = iodd + i 

        isum = ieven - iodd  
        iNo = iNo// 10

    print(isum)


def main():
    iValue = 0 

    try : 
        iValue = int(input("Enter a number :"))
    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__":main()
"""
Enter a number :2395
-15
vedantbarne@Vedants-MacBook-Air-2 Assignment_13 % python3 a13_5.py
Enter a number :1018
6
vedantbarne@Vedants-MacBook-Air-2 Assignment_13 % python3 a13_5.py
Enter a number :8440
16
"""
