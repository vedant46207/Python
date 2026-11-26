import sys

def display(iRow , iCol):
    iCount = 0 
    ch = '\0'
    for i in range (1 , iRow +1):
        if i%2 ==0: iCount = 1 
        else : ch = 'a'
        for j in range (1, iCol+1):
            if i%2 == 0 : print(j, end = "\t")
            else : print(ch, end = "\t")

            ch = chr(ord(ch)+1)
            iCount +=1

        print() 


def main():
    iValue1 = 0
    iValue2 = 0 

    try : 
        iValue1 = int(input("Enter number of rows: "))
        iValue2 = int(input("Enter number of columns :"))

    except ValueError : 
        print("Invalid input ", file = sys.stderr  )
        sys.exit(1)

    display(iValue1, iValue2 )

if __name__ == "__main__": main()

"""
Enter number of rows: 5
Enter number of columns :5
a	b	c	d	e	
1	2	3	4	5	
a	b	c	d	e	
1	2	3	4	5	
a	b	c	d	e	
▲ Assignment_17 main › python3 a17_3.py
Enter number of rows: 4
Enter number of columns :5
a	b	c	d	e	
1	2	3	4	5	
a	b	c	d	e	
1	2	3	4	5
"""

