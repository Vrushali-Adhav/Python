''' 
   Program Name            : Accept a classroom number from user and display class
                            for example 35- FYBCS A
                                        36-FYBCS B
                                        37-SYBCS A
                                        38-SYBCS B
                                        39-TYBCS
     Programming language : Python                                
    Programmer's Name     : Adhav Vrushali Abasaheb
    Date                  : 29 July 2022
'''

print("35")
print("36")
print("37")
print("38")
print("39")

classno=int(input("Enter your class room number"))

if(classno==35):
    print("35 - FYBCS A")
elif(classno==36):
    print("36 -FYBCS B")
elif(classno==37):
    print("37 - SYBCS A")
elif(classno==38):
    print("38 - SYBCS B")
elif(classno==39):
    print("39 - TYBCS")
else:
    print("Invalid Class number")
    
