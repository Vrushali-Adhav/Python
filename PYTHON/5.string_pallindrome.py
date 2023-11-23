'''
        Program Name         : Accept string from user and check it is palindrome or not.
        Promamming Language  : Python
        Programmer's Name    : Adhav Vrushali Abasaheb
        Date                 : 29 July 2022
'''
#accept string

string=input("enter your string : ")


#travels string  in forward direction
str1=string[0:]

#travels string  in reversr direction
str2=string[::-1]

#check travels of forward direction is equal to reverse direction string
if(str1==str2):
     print("Yes\n{} is  pallindrome".format(string))
else:
    print(" No\n{} is not pallindrome".format(string))
    
      
        
