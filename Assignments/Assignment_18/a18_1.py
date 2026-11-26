import sys

def display(iRow , iCol):
    for i in range (1, iRow +1):
        for j in range (1 , i+1):
            print("*", end = "\t")

        for j in range (i , iCol):
            print("#", end = "\t")
        

        print()




def main():
    iValue1 = 0 
    iValue2 =0 

    try : 
        iValue1 = int(input("Enter number of rows :"))
        iValue2 = int(input("Enter number of columns :"))

    except ValueError : 
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2)

if __name__ == "__main__": main()

"""
Enter number of rows :4
Enter number of columns :4
*	#	#	#	
*	*	#	#	
*	*	*	#	
*	*	*	*	
▲ Assignment_18 main › python3 a18_1.py
Enter number of rows :4
Enter number of columns :5
*	#	#	#	#	
*	*	#	#	#	
*	*	*	#	#	
*	*	*	*	#	
▲ Assignment_18 main › python3 a18_1.py
Enter number of rows :5
Enter number of columns :6
*	#	#	#	#	#	
*	*	#	#	#	#	
*	*	*	#	#	#	
*	*	*	*	#	#	
*	*	*	*	*	#
"""
