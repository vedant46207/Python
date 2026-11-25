import sys

def display(iRow , iCol):
    i = 0 
    j = 0 
    ch = 'A'
    for i in range (1, iRow +1):
        
        for j in range ( 1 , iCol+1):
            print(ch, end = "\t")
        ch  = chr(ord(ch)+1)
        print()
        
def main():

    iValue1 = 0 
    iValue2 = 0 

    try : 
        iValue1 = int(input("Enter number of rows: "))
        iValue2 = int(input("Enter number of columns :"))

    except ValueError :
        print("Invalid input ", file = sys.stderr)
        sys.exit(1)

    display(iValue1, iValue2)

if __name__ == "__main__":main()

"""
Enter number of rows: 4
Enter number of columns :4
A	A	A	A	
B	B	B	B	
C	C	C	C	
D	D	D	D	
▲ Assignment_16 main › python3 a16_3.py
Enter number of rows: 5
Enter number of columns :6
A	A	A	A	A	A	
B	B	B	B	B	B	
C	C	C	C	C	C	
D	D	D	D	D	D	
E	E	E	E	E	E
"""

