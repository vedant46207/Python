import sys

def display(iNo):
    for i in range (1, 1+iNo):
        print("$", end = "\t")
        print("*", end = "\t")

    print()

def main():
    iValue = 0 

    try : iValue = int(input("Enter a number :"))
    except ValueError : 
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__": main()

"""
Enter a number :5
$	*	$	*	$	*	$	*	$	*	
vedantbarne@Vedants-MacBook-Air-2 Assignment_7 % python3 a7_1.py
Enter a number :3
$	*	$	*	$	*
"""

