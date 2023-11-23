''' Program Name   :
                       write a function which accept a number and return True if
                       number is Even and return False if number is Odd.

Programmer's Name  :    Adhav Vrushali Abasaheb
Programming language: PYTHON

Date            : 17 Aug 2022
                              '''

number=int(input("enter a number = "))
def even_odd_number(num):
    if num%2==0:
        return True
    else:
        return False
numbr = even_odd_number(number)
if numbr==True:
    print("number is even")
else:
    print("number is odd")
    
