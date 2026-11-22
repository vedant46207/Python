import sys
def display(ch):
    if(ch >= 'a' and ch <= 'z'): ch = chr(ord(ch) -32 ) 
    elif (ch >= 'A' and ch <= 'Z') : ch = chr(ord(ch) +32 )

    return ch


def main():
    cValue = '\0'

    try : cValue = (input("Enter a char :"))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    if len(cValue) != 1 :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    print(display(cValue ))
    print()

if __name__ == "__main__": main()
"""
vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_4.py
Enter a char :a
A

vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_4.py
Enter a char :A
a

vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_4.py
Enter a char :h
H

vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_4.py
Enter a char :ab
Invalid input
"""