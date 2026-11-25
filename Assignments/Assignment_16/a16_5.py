import sys

def display(iRow , iCol):
    iCount = 1 
    for i in range (1, iRow +1):
        for j in range (1, iCol +1):
            print(iCount , end = "\t")
            iCount +=1 
        print()
        



def main():
    
    iValue1 = 0 
    iValue2 = 0 

    try : 
        iValue1 = int(input("Enter number of rows: "))
        iValue2 = int(input("Enter number of columns :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2)

if __name__ == "__main__":main()
"""
Enter number of rows: 3
Enter number of columns :4
1	2	3	4	
5	6	7	8	
9	10	11	12	
▲ Assignment_16 main › python3 a16_5.py
Enter number of rows: 4
Enter number of columns :4
1	2	3	4	
5	6	7	8	
9	10	11	12	
13	14	15	16
"""