import sys

def display(iNo1 , iNo2):
    if(iNo2 > iNo1 ):
        for i in range (iNo1, iNo2+1):
             print(i, end = "\t")
    elif (iNo1 == iNo2 ): print("Both numbers are same ")
    else :
         for i in range (iNo2, iNo1+1):
             print(i, end = "\t")
    print()

    
def main():
    iValue1 = 0
    iValue2 = 0 

    try :
        iValue1 = int(input("Enter number :"))
        iValue2 = int(input("Enter number :"))

    except ValueError : 
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2 )

if __name__ == "__main__": main()


"""
Enter number :23
Enter number :23
Both numbers are same 

vedantbarne@Vedants-MacBook-Air-2 Assignment_11 % python3 a11_1.py
Enter number :23
Enter number :25
23	24	25	
vedantbarne@Vedants-MacBook-Air-2 Assignment_11 % python3 a11_1.py
Enter number :23
Enter number :35
23	24	25	26	27	28	29	30	31	32	33	34	35
"""