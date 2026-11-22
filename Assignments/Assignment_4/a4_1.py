import sys 

def display(iNo):

    if iNo == 0 : print("Equal to zero")
    elif iNo > 0 : print("greater than zero ")
    else : print("Less than zero ")

def main():
    iValue = 0
    iRet = 0 

    try : iValue = int(input("Enter a number :")) 
    except ValueError : 
        print("Invalid input ", files = sys.stderr )
        sys.exit(1)

    display(iValue )

if __name__ ==  "__main__" : main()

"""
Enter a number :9
greater than zero 
vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_1.py
Enter a number :-1
Less than zero 
vedantbarne@Vedants-MacBook-Air-2 Assignment_4 % python3 a4_1.py
Enter a number :0
Equal to zero
"""
