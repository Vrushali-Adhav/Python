'''
    Program Name         : Lucky Draw System For Hotel Bill Pay
    
    Programming Language : Python
    
    Programmer's Name    : Adhav Vrushali Abasaheb
    
    Date                 :  1 Aug 2022


'''
#Accept friends name for choising who will pay hotel bill
s=input("enter friends name : ")

#split function will return string in list data type
p=s.split()

#import random package for choices
import random

#random.choices will accept list and return one random element of list
n= random.choices(p)

#now print who's name is randomly selected for hotel bill payment
print(" \n\nCongratulations {} You are selected for hotel bill payment ".format(n))

