import sys

def display(iNo1 , iNo2):
    if(iNo2 > iNo1 ):
        for i in range (iNo1, iNo2+1):
             if i%2 ==0 :print(i, end = "\t")
    elif (iNo1 == iNo2 ): print("Both numbers are same ")
    else :
         for i in range (iNo2, iNo1+1):
            if i%2 ==0 :print(i, end = "\t")
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
Enter number :35
24	26	28	30	32	34	
vedantbarne@Vedants-MacBook-Air-2 Assignment_11 % python3 a11_2.py
Enter number :23
Enter number :23
Both numbers are same 

vedantbarne@Vedants-MacBook-Air-2 Assignment_11 % python3 a11_2.py
Enter number :-10
Enter number :2
-10	-8	-6	-4	-2	0	2
"""