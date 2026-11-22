import sys
def display(iNo, iFrequency):
    if iFrequency < 0 :
        iFrequency = -iFrequency 

    for i in range (iFrequency):
        print(iNo, end ="\t")

    print()


def main():
    try :
        iValue1 = int (input ("Enter first number :"))
        iValue2 = int (input("Enter second number :"))

    except ValueError : 
        print("Invalid input " , file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2)

if __name__ == "__main__":
    main()

"""
Enter second number :4
5	5	5	5	
vedantbarne@Vedants-MacBook-Air-2 Assignment_2 % python3 a2_4.py
Enter first number :9 
Enter second number :2
9	9	
"""