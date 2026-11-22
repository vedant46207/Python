import sys

def display(iNo):

    for i in range (1, (iNo//2)+1):
        if iNo%i == 0 :
            print(i, end = "\t")

    print()

def main():
    iValue = 0 

    try:
        iValue = int(input("Enter a number: "))
    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

    return 0 

if __name__ == "__main__":main()

"""
Enter a number: 12
1	2	3	4	6	
vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_2.py
Enter a number: 18
1	2	3	6	9	
"""