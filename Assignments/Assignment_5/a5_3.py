import sys

def displayGrade(fMarks):
    if(fMarks < 0 or fMarks > 100):print("Invalid Marks")
    elif(fMarks >= 90):print("Grade A")
    elif(fMarks >= 75):print("Grade B")
    elif(fMarks >= 60):print("Grade C")
    elif(fMarks >= 40):print("Grade D")
    else : print("Fail")


def main():
    fMarks = 0.0

    try : 
        fMarks = float(input("Enter marks :"))

    except ValueError:
        print("Invalid input", file = sys.stderr)
        sys.exit(1)

    displayGrade(fMarks)

if __name__ == "__main__": main()

"""
Enter marks :85
Grade B
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_3.py
Enter marks :35
Fail
vedantbarne@Vedants-MacBook-Air-2 Assignment_5 % python3 a5_3.py
Enter marks :105
Invalid Marks
"""