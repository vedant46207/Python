import sys

def display(iNo):
    i = 0 
    iMul = 1 

    if iNo<0: iNo = -iNo
    if iNo ==0 : print(iNo)

    while iNo!=0 :
        i = iNo%10
        if(i!=0): iMul = iMul *i 
        iNo = iNo// 10

    print(iMul)


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
270
vedantbarne@Vedants-MacBook-Air-2 Assignment_13 % python3 a13_4.py
Enter a number :1018
8
vedantbarne@Vedants-MacBook-Air-2 Assignment_13 % python3 a13_4.py
Enter a number :-1018
8
"""
