l=['Paneer','chicken','Pav Bhaji','chicken Tandoor','chicken masala','kabab chicken']
'''def check(x):
    ret="chicken" in x
    return ret

lambda x : "chicken"in x
'''

p= list(filter(lambda x : "chicken"in x,l))
print(p)
