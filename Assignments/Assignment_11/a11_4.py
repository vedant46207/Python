import sys


def display(iNo1 , iNo2):
    iSum = 0 
    if(iNo2 > iNo1 ):
        for i in range (iNo1, iNo2+1):
             if i%2 ==0 :iSum = iSum + i
    elif (iNo1 == iNo2 ): print("Both numbers are same ")
    else :
         for i in range (iNo2, iNo1+1):
            if i%2 ==0 :iSum = iSum + i
    print(iSum)

    
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
Enter number :30
108
vedantbarne@Vedants-MacBook-Air-2 Assignment_11 % python3 a11_4.py
Enter number :-10
Enter number :2
-28
vedantbarne@Vedants-MacBook-Air-2 Assignment_11 % python3 a11_4.py
Enter number :10
Enter number :18
70
"""