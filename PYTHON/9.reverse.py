'''
   Program Name         : Reverse the Number
   Programming Language :Python
   Programmer's Name    : Adhav Vrushali Abasaheb
   Date                 : 15 Aug 2022
   
'''
num = int(input("enter a number = "))
rev_num=0
while num!=0:   
    number   =  num%10
    rev_num  =  rev_num*10+number
    num     //=  10
print(f"reverse = ",rev_num)
