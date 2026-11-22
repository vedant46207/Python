import sys
def display(iNo):
    for i in range(1, 1+iNo):
        print(i*2, end = "\t")

    print()


def main():
    iValue = 0 

    try :
        iValue = int (input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__" :main()

"""
Enter number :7
2	4	6	8	10	12	14	
vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_1.py
Enter number :9
2	4	6	8	10	12	14	16	18	
"""
