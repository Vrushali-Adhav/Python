'''
    Program Name         :    Accept user's age and Display user's  remaining days,weeks , months ,years means life span.
    Programming language  :   Python
    Programmer's Name    :    Adhav Vrushali Abasaheb
    Date                 :    29 July 2022
    '''
#accept user's age and store in age
age=int(input("enter your age"))

#calculate user's remaing days using formula
#remaining days =  (90- age )*365
r_days = (90 - age)*365
print("you have  {}  days".format(r_days))

#calculate user's remaining week using formula
#remaining week's= (90-age )*52
r_weeks = (90 - age)*52
print("you have  {}  weeks".format(r_weeks))

#calculate user's remaining months using formula
#remaining month's=(90-age)*12
r_months = (90 - age)*12
print("you have  {}  months".format(r_months))

#calculate user's remaining years using formula
#remaining year's=90-age
r_years = 90 - age
print("you have  {}  years".format(r_years))

print("enjoy your LIFE joyfully")

