import sys

def display(iNo):

    if iNo<0 : iNo = -iNo

    for i in range (1, 11 ):
        print("*", end = "\t")

    for i in range (1, iNo+1 ):
            print("#", end = "\t")


def main():
    iValue = 0 

    try :
        iValue = int(input("Enter number :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter number :5
*	*	*	*	*	*	*	*	*	*	#	#	#	#	#	%


Enter number :-3


*	*	*	*	*	*	*	*	*	*	#	#	#	%    


Enter number :4
*	*	*	*	*	*	*	*	*	*	#	#	#	#	%        	
"""

