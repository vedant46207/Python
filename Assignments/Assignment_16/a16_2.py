import sys

def display(iRow , iCol):
    for i in range (1, iRow +1 ):
        if i%2 == 0 : ch = 'a'
        else : ch = 'A'
        for j in range (1, iCol+1):
            print(ch, end = "\t")
            ch = chr (ord(ch) +1)
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
A	B	C	D	
a	b	c	d	
A	B	C	D	
a	b	c	d	
▲ Assignment_16 main › python3 a16_2.py
Enter number of rows: 5
Enter number of columns :6
A	B	C	D	E	F	
a	b	c	d	e	f	
A	B	C	D	E	F	
a	b	c	d	e	f	
A	B	C	D	E	F
"""