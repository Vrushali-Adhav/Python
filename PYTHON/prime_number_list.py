'''Program Name:separation of list into prime and not prime
   Programmer's Name:Adhav Vrushali Abasaheb
   Date:14 August 2022'''







l_number=[1,2,3,4,5,6,7,8,9]
l_prime=[]
l_not_prime=[]

for j in l_number:
    flag=False
    for i in range(2,j):
        if j%i==0:
            flag=True
            break
    if flag==True:
        l_not_prime.append(j)
    else:
        l_prime.append(j)
print(l_prime)
print(l_not_prime)
        
    
