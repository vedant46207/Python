import sys

def display(iNo):
    isum = 0 
    if iNo < 0 : iNo = -iNo
    for i in range (1 , iNo+1):
        if(iNo%i !=0):
            isum = isum +i 

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
Enter a number :12
50
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_4.py
Enter a number :10
37
"""
