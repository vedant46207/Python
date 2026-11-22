
def Display(iNo):

    for i in range (1, iNo +1):
        print("*\t", end = "")

    print()

def main():
    iValue = 0 
    print("Enter a number :", end = "")

    try : iValue = int(input ())
    except ValueError:
        print("Invalid input")
        return 1

    Display(iValue ) 


if __name__ == "__main__":
    main()

"""
Enter a number :4
*	*	*	*	


vedantbarne@Vedants-MacBook-Air-2 Assignment_2 % python3 a2_2.py
Enter a number :6
*	*	*	*	*	*	
"""