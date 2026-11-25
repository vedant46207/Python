import sys

def display(iRow , iCol):
    for i in range (iRow, 0 , -1 ):
        for j in range (1, iCol+1):
            print ( i , end = "\t")
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
Enter number of rows: 4
Enter number of columns :5
4	4	4	4	4	
3	3	3	3	3	
2	2	2	2	2	
1	1	1	1	1	
▲ Assignment_16 main › python3 a16_4.py
Enter number of rows: 6
Enter number of columns :7
6	6	6	6	6	6	6	
5	5	5	5	5	5	5	
4	4	4	4	4	4	4	
3	3	3	3	3	3	3	
2	2	2	2	2	2	2	
1	1	1	1	1	1	1
"""