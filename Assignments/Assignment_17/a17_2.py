import sys

def display(iRow , iCol):
    iCount  =1 
    for i in range (1 , iRow +1):
        if i%2 ==0: iCount = 1 
        else : iCount = 2
        for j in range (1, iCol+1):
            print(iCount , end = "\t")
            iCount +=2 

        print() 


def main():
    iValue1 = 0
    iValue2 = 0 

    try : 
        iValue1 = int(input("Enter number of rows: "))
        iValue2 = int(input("Enter number of columns :"))

    except ValueError : 
        print("Invalid input ", file = sys.stderr  )
        sys.exit(1)

    display(iValue1, iValue2 )

if __name__ == "__main__": main()

"""
Enter number of rows: 4
Enter number of columns :4
2	4	6	8	
1	3	5	7	
2	4	6	8	
1	3	5	7	
▲ Assignment_17 main › python3 a17_2.py
Enter number of rows: 5
Enter number of columns :6
2	4	6	8	10	12	
1	3	5	7	9	11	
2	4	6	8	10	12	
1	3	5	7	9	11	
2	4	6	8	10	12
"""

