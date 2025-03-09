def fact(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

# n = int(input("Enter any number: "))
n = 5
m = 6
o = 7
p = 8
result1 = fact(n)
result2 = fact(m)
result3 = fact(o)
result4 = fact(p)
print(n,"factorial is",result1)
print(m,"factorial is",result2)
print(o,"factorial is",result3)
print(p,"factorial is",result4)