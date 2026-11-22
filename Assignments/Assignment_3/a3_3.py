import sys

def display(iNo):

    for i in range (1, (iNo // 2)+1):
        if(iNo%i ==0 ):
            if(i%2 ==0):
                print(i, end ="\t")

    print()


def main():
    iValue = 0 

    try: iValue = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__":main()
"""
Enter a number: 12
2	4	6	
vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_3.py
Enter a number: 36
2	4	6	12	18	
vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_3.py
Enter a number: 9

vedantbarne@Vedants-MacBook-Air-2 Assignment_3 % python3 a3_3.py
Enter a number: 10
2	
"""