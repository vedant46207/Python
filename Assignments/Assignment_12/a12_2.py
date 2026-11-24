import sys

def display(iNo):
    i = 0 
    iCount = 0 
    if iNo<0: iNo = -iNo
    if iNo ==0 : print(iNo)

    while iNo!=0 :
        i = iNo%10
        if i == 0 : iCount +=1
        iNo = iNo// 10

    if(iCount == 0) : print("No zeros")
    else : print(iCount)


def main():
    iValue = 0 

    try : 
        iValue = int(input("Enter a number ;"))
    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__":main()
"""
Enter a number ;2395
No zeros
vedantbarne@Vedants-MacBook-Air-2 Assignment_12 % python3 a12_2.py
Enter a number ;3200
2
"""
