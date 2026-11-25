import sys

def display(iNo):
 
    if iNo < 0 : iNo = -iNo
    for i in range ((iNo//2), 1, -1 ):
        if(iNo%i ==0):
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
6	4	3	2	
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_2.py
Enter a number :13

vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_2.py
Enter a number :10
5	2
"""
