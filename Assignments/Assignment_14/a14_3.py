import sys

def display(iNo):

    if iNo < 0 : iNo = -iNo
    for i in range (1 , iNo+1):
        if(iNo%i !=0):
            print(i, end = "\t")

    print()


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
5	7	8	9	10	11	
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_3.py
Enter a number :13
2	3	4	5	6	7	8	9	10	11	12	
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_3.py
Enter a number :10
3	4	6	7	8	9	
"""
