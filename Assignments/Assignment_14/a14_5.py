import sys

def display(iNo):
    isumodd = 0 
    isumeven = 0 
    if iNo < 0 : iNo = -iNo
    for i in range (1 , iNo+1):
        if(iNo%i !=0):
            isumodd = isumodd +i 
        else : isumeven = isumeven + i 


    print(isumeven- isumodd)


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
-22
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_5.py
Enter a number :10
-19
"""
