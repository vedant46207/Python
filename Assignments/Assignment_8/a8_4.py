import sys

def display(iNo):

    if iNo<0 : iNo = -iNo

    for i in range (1 , 11 ):
        print(iNo*i, end = "\t")

    print()



def main():
    iValue = 0 
    iRet = 0

    try :
        iValue = int(input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter number :5
5	10	15	20	25	30	35	40	45	50	
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_4.py
Enter number :6
6	12	18	24	30	36	42	48	54	60	
vedantbarne@Vedants-MacBook-Air-2 Assignment_8 % python3 a8_4.py
Enter number :4
4	8	12	16	20	24	28	32	36	40	
"""

