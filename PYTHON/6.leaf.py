'''
     Program Name: Leaf Year checking second way
     Programmer Name : Vrushali Abasaheb Adhav
     Date            : 29 july 2022
     '''

#accept year
year=int(input("enter year"))

#check year%400 == 0 && year%100==0 or not if yes it is leaf
if ( year%400 == 0 and year%100==0):
    print("year is leaf")

    
#check year%100 != 0 && year%4==0 or not if yes it is   leaf    
elif (year%100!=0 and year%4==0):
    print("year is leaf year")


else:
    print("year is not leaf")
