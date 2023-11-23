'''
    Program Name          : LOVE CALCULATOR
    Programming Language  : PYTHON
    Programmers Name      : Adhav Vrushali Abasaheb
    Date                   :29 July 2022
'''
print("*******LOVE Calculator*********\n")

#Accept your  Name
name1 = input("Enter your name = ")
#Accept your partners Name
name2 = input("enter your partners name = ")

#combine two names in name
name = name1 + name2
#convert string into capital 
name = name.upper()


#find count of L O V E
L = name.count("L")
O = name.count("O")
V = name.count("V")
E = name.count("E")
# Combine count of L O V E
First =L+O+V+E

#find count of T R U E
T = name.count("T")
R = name.count("R")
U = name.count("U")
E = name.count("E")
#combine count of T R U E
second=T+R+U+E
#concat first and secon and display Love

print("Your Love is {}{}%".format(First,second))

