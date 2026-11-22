import sys
def display(ch):
    if(
        ch == 'A' or ch == 'E' or ch == 'I' or ch == 'U' or ch == 'O'
        or
        ch == 'a' or ch == 'e' or ch == 'i' or ch == 'u' or ch == 'o'
        ): return True
    else :return False


def main():
    cValue = '\0'
    bRet = False 

    try : cValue = (input("Enter a char :"))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    if len(cValue) != 1 :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    bRet = (display(cValue ))
    if(bRet == True) : print("TRUE")
    else : print("FALSE")

    print()

if __name__ == "__main__": main()
"""
Enter a char :a
TRUE

vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_5.py
Enter a char :E
TRUE

vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_5.py
Enter a char :N
FALSE
"""