def Display(iNo) :

    for i in range (1, iNo +1 ):
        print("*\t", end ="")

    print()

def main():
    iValue = 0 

    print("Enter a number :")
    try :
        iValue = int (input())
    except ValueError:
        print("Invalid input")
        return 1
    if(iValue < 0) : iValue = -iValue

    Display(iValue)
    return 0 

if __name__ == "__main__":
    main()

"""
Enter a number :
6
*	*	*	*	*	*	


vedantbarne@Vedants-MacBook-Air-2 Assignment_1 % python3 a1_5.py
Enter a number :
5
*	*	*	*	*	
"""