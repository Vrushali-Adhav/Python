
'''
    Program Name:Accept a number from user and create list of that many elements.
                 then accept another element from user and remove all occurence of that number.
                 example -
                         input num=5
                         now add five num in list[10,20,10,30,20]
                         now accept another number i.,e20
                         now delete all 20 from list.

                         final output [10,10,30].
   Programmer's Name:Adhav Vrushali Abasaheb
   Programming language:Python
   Date                :25 Aug 2022'''
num=int(input("enter a number"))
l=[]
for i in range(num):
    value=int(input("enter value"))
    l.append(value)
print(l)
num1=int(input("enter element to remove its occurence"))
for i in (0,num):
    l.remove(num1)
print(l)    
