def my_fun(Num1):
    print(f"value of Num1 in my_fun{Num1}")
    Num1=Num1+10
    print(f"value of Num1 in my_fun{Num1}")
value = 50
print(f"before function call value = {value}")
my_fun(value)
print(f"After Function call value = {value}")
    
