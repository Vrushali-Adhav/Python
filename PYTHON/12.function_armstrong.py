





'''Program Name : Function for armstrong number
   Progrmmer's Name:Adhav Vrushali Abasaheb
   Programming language:Python
   Date :17 Aug 2022'''

def armstrong(num):#153
    Sum=0
    cnt=0
    temp=num#temp=153
    while num>0:
        digit=num%10#153%10
        cnt=cnt+1
        num=num//10

    num=temp
    while temp>0:
        
        digit=temp%10
        Sum=Sum+digit**cnt
        temp=temp//10
    if Sum==num:
        return True
    else:
        return False

num=int(input("enter number"))#153
ret=armstrong(num)
if ret==True:
    print("number is armstrong")
else:
    print("number is not armstron")
         
    







