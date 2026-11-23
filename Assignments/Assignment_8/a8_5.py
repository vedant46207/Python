import sys

def display(iNo):

    if iNo<0 : iNo = -iNo

    for i in range (10 ,0, -1 ):
        print(iNo*i, end = "\t")

    print()



def main():
    iValue = 0 

    try :
        iValue = int(input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter number :5
50	45	40	35	30	25	20	15	10	5	
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_5.py
Enter number :3
30	27	24	21	18	15	12	9	6	3	
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_5.py
Enter number :9
90	81	72	63	54	45	36	27	18	9		
"""

