def check10(iNo):
    if (iNo > 10): return True
    else : return False 


def main():
    iValue = 0 
    bRet = False 

    print("Enter a number :", end = "")

    try : iValue = int (input ())
    except ValueError :
        print("Invalid input ")
        return 1

    bRet = check10(iValue)
    if(bRet == True) : print("Hello")
    else : print("Demo")



if __name__ == "__main__":
    main()

"""
Enter a number :5
not greater than 10
vedantbarne@Vedants-MacBook-Air-2 Assignment_2 % python3 a2_3.py
Enter a number :11
Greater than 10
vedantbarne@Vedants-MacBook-Air-2 Assignment_2 % python3 a2_3.py
Enter a number :10
not greater than 10
"""