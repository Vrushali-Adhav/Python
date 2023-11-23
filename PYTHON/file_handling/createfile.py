#fd = open("Hello.txt",'x') #for ceating file this line is used x is mode for creating
#fd = open("Hello.txt",'w')#for writing in file
#fd = open("Hello.txt",'a')
#data = input("enter data ")#asking to user for writing in file
fd = open("Hello.txt",'r')
print(fd.read(3))
#print kel je read je te first 3 character will print
#fd.write(data)
#fd madhe ghetl user ne dilel ani write ne to data file madhe lihila
#write ne aapan jar next time file open kele write karayla 
#tar aadhicha data erase zalela asto ani start la offset asto means curssor....
#tyasathi append mode ahe ki jyamul aadhicha pan data asto means concatenation hot
#append last la jaun thambt jar file empty asel tar first la start hot
#file read mode madhe kele tar fact read hot tyat write nahi karta yet
#file write mode madhe kele tar fact write hot tyat read nahi karta yet