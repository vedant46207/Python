def checkDivby5(iNo):
    if(iNo %5 == 0):return True 
    else : return False 

def main():
    iValue = 0 
    bRet = False 

    print("Enter a numher ;" , end="")
    try :
        iValue = int(input())
    except ValueError:
        print("Invalid input")
        return 1 
    bRet = checkDivby5(iValue)
    if(bRet == True): print("Divisible by 5")
    else : print("Not divisible by 5")

    return 0 

if __name__ == "__main__":
    main()

"""
vedantbarne@Vedants-MacBook-Air-2 Assignment_1 % python3 a1_4.py
Enter a numher ;15
Divisible by 5

vedantbarne@Vedants-MacBook-Air-2 Assignment_1 % python3 a1_4.py
Enter a numher ;20
Divisible by 5
"""