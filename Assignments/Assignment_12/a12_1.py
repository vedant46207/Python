import sys

def display(iNo):
    i = 0 
    if iNo<0: iNo = -iNo
    if iNo ==0 : print(iNo)

    while iNo!=0 :
        i = iNo%10
        print(i)
        iNo = iNo// 10

    print()


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
5
9
3
2

vedantbarne@Vedants-MacBook-Air-2 Assignment_12 % python3 a12_1.py
Enter a number ;1018
8
1
0
1

vedantbarne@Vedants-MacBook-Air-2 Assignment_12 % python3 a12_1.py
Enter a number ;-1018
8
1
0
1

vedantbarne@Vedants-MacBook-Air-2 Assignment_12 % python3 a12_1.py
Enter a number ;9000 
0
0
0
9
"""
