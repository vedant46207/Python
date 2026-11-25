import sys

def display(iNo):
    imul =1 
    if iNo < 0 : iNo = -iNo
    for i in range (1 , (iNo//2)+1 ):
        if(iNo%i ==0):
            imul = imul*i 

    print(imul)


def main():
    iValue = 0 

    try : 
        iValue = int(input("Enter a number :"))
    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue)

if __name__ == "__main__":main()
"""
Enter a number :12
144
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_1.py
Enter a number :13
1
vedantbarne@Vedants-MacBook-Air-2 Assignment_14 % python3 a14_1.py
Enter a number :10
10
"""
