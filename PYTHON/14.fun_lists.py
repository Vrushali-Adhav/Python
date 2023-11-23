'''
   Program Name: write a function which accept a list and one integer number...

                 if we get 1 as a second parameter sort list in assending order.

                 if we get 2 as a second parameter sort list in decending order.

                 example:
                 list[19,5,35]
                 function call
                 fun(list,1)
                 output-[5,19,35]
                 function call
                 fun(list,2)
                 output-[35,19,5]
                 Note -Value should be same of original list after function call

                 function call chya aadhi ani nantr list madhil value same print zalya pahije.
                 output function madhe print kele tri chalel.

    Programmer's Name: Adhav Vrushali Abasaheb
    Programming language: Python
    Date                 :25 Aug 2022'''

def fun(lists,num):
    list2=lists.copy()
    if num==1:
        list2.sort(reverse=False)
        print(list2)
    elif num==2:
        list23.sort(reverse=True)
        print(list2)
    else:
        print("sorry pass second parameter as 1 or 2")

lists=[19,2,35]
print("list before function call\n")
print(lists)
print("\nlist after passing parameter 2 as a second parameter")
fun(lists,2)
print("\nlist after passing parameter 1 as a second parameter")
fun(lists,1)
print("\nlist after function call")
print(lists)

















        
    
        
