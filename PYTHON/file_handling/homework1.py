#read first 5 lines from paragraph
#fd = open("para.txt",'r+')
#print(fd.tell())
#tell fun give position of offset
#fd.seek(1)
#print(fd.tell())
#print(fd.readline())
#fd.seek(2)
#print(fd.readline())
#fd.seek(3)
#print(fd.readline())
#fd.seek(4)
#print(fd.readline())
#fd.seek(5)
#print(fd.readline())

nol = int(input("enter how many lines you want to run"))
if nol<=0:
   print("invalid")
   sys.exit()

    
    

fd = open('para.txt','r')
l = fd.readlines()
for i in range l[-5:]:
    print(i)

fd.close()