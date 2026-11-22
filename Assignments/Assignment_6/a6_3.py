import sys

def display(iNo):
    if iNo <= 100 : print("Bill : ",iNo*5)
    elif iNo >100 and iNo < 200 : print("Bill : ",iNo*7)
    elif iNo > 200 : print("Bill : ",iNo*10)

def main():

    iValue = 0 

    try :
        iValue = int(input ("Enter units :"))

    except ValueError :
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    display(iValue)



if __name__ == "__main__": main()

"""
Enter units :80
Bill :  400
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_3.py
Enter units :150
Bill :  1050
vedantbarne@Vedants-MacBook-Air-2 Assignment_6 % python3 a6_3.py
Enter units :250
Bill :  2500
"""