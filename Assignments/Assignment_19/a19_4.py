import sys 

def display(iRow ,iCol):
    for i in range (1 , iRow +1):
        for j in range (1 , iCol+1): 
            if (i == j ):print("*", end = "\t")
            elif(i ==1 or i== iRow ) :print("*", end = "\t")
            elif(j == 1 or j == iCol) :print("*", end = "\t")
            else:  print(" ", end = "\t")
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
Enter number of rows: 5
Enter number of columns: 5
*	*	*	*	*	
*	*	 	 	*	
*	 	*	 	*	
*	 	 	*	*	
*	*	*	*	*	
▲ Assignment_19 main › python3 a19_4.py
Enter number of rows: 6
Enter number of columns: 6
*	*	*	*	*	*	
*	*	 	 	 	*	
*	 	*	 	 	*	
*	 	 	*	 	*	
*	 	 	 	*	*	
*	*	*	*	*	*
"""
    