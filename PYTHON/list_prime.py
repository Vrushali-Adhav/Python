l_num=[12,3,5,45,6,76,32,22]
l_prime=[]
l_not_prime=[]
flag=False
for i in range(l_num):
    if num % i==0:
        l_not_prime.append(i)
    else:
        l_prime.append(i)
print(l_prime)
print(l_not_prime)
        
   
