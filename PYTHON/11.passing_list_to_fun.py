def my_fun(l):
    print(f"value of Num1 in my_fun{l}")
    l.append(20)
    print(f"value of Num1 in my_fun{l}")
l = [50]
print(f"before function call value = {l}")
my_fun(l)
print(f"After Function call value = {l}")
    
