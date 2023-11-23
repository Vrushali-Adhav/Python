'''
     Program Name: Leaf Year checking
     Programmer Name : Vrushali Abasaheb Adhav
     Date            : 29 july 2022
     '''

#accept year
year=int(input("enter year"))

#check year%400 == 0 or not if yes it is leaf
if  year%400 == 0:
    print("year is leaf")

#check year%100 == 0 or not if yes it is  not leaf    
elif year%100==0:
    print("year is'nt leaf year")

#check year%4 == 0 or not if yes it is leaf
elif year%4==0:
    print("year is leaf")
else:
    print("year is not leaf")
