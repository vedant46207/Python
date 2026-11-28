import sys

def display(iRow ,iCol):
    for i in range (1, 1+iRow ):
        for j in range (1, iCol+1):
            if j%2 ==0 : print("#", end = "\t")
            else : print("*", end = "\t")

        print()


def main():
    iValue1 = 0
    iValue2 = 0 

    try :
        iValue1 = int(input ("Enter number of rows :"))
        iValue2 = int(input ("Enter number of columns :"))
    except ValueError :
        print("Invalid Input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2 )

if __name__ == "__main__": main()

"""
Enter number of rows :4
Enter number of columns :4
*	#	*	#	
*	#	*	#	
*	#	*	#	
*	#	*	#	
▲ Assignment_21 main › python3 a21_4.py
Enter number of rows :5
Enter number of columns :5
*	#	*	#	*	
*	#	*	#	*	
*	#	*	#	*	
*	#	*	#	*	
*	#	*	#	*
"""
