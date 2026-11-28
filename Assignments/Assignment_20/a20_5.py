import sys 

def display(iRow ,iCol):
    for i in range ( 1 , iRow +1):
        for j in range (1 , iCol+1):
            if i == j : print(j , end = "\t")
            elif (i ==1 or i== iRow or j==1 or j==iCol):
                print(j, end = "\t")
            else : print(" ", end = "\t")
        print()


def main():
    iValue1 = 0
    iValue2 = 0

    try :
        iValue1 = int(input("Enter number of rows: "))
        iValue2 = int(input("Enter number of columns: "))

    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1 , iValue2 )

if __name__ == "__main__":
    main()
"""
Enter number of rows: 4
Enter number of columns: 4
1	2	3	4	
1	2	 	4	
1	 	3	4	
1	2	3	4	
▲ Assignment_20 main › python3 a20_1.py
Enter number of rows: 6
Enter number of columns: 6
1	2	3	4	5	6	
1	2	 	 	 	6	
1	 	3	 	 	6	
1	 	 	4	 	6	
1	 	 	 	5	6	
1	2	3	4	5	6
"""
    