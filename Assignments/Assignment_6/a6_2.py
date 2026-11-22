import sys

def display(iNo):
    if (iNo <1000): print("Payable amount :",iNo)
    elif (iNo >=1000 and iNo<5000): print("Payable amount :",0.9*iNo)
    elif (iNo>=5000): print("Payable amount :",0.8*iNo)

def main():

    iValue = 0 

    try :
        iValue = int(input ("Enter total amount :"))

    except ValueError :
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    display(iValue)



if __name__ == "__main__": main()

"""
Enter total amount :800
Payable amount : 800
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_2.py
Enter total amount :2000
Payable amount : 1800.0
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_2.py
Enter total amount :6000
Payable amount : 4800.0
"""