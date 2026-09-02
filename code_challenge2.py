#VARIABLES
amount = eval(input("Enter Money to DEPOSIT ---->>> ")) 
print("Money to deposit --->", amount)
#print(type(amount))

#computation here
s = amount // 1000
amount1 = amount % 1000
p = amount1 // 500
amount2 = amount1 % 500
i = amount2 // 200
amount3 = amount2 % 200
d = amount3 // 100
amount4 = amount3 % 100
e = amount4 // 50
amount5 = amount4 % 50
r = amount5 // 20
amount6 = amount5 % 20
m = amount6 // 10
amount7 = amount6 % 10
a = amount7 // 5
amount8 = amount7 % 5
n = amount8 // 1
amount9 = amount8 % 1


print("Ph denomination")


print("1000 -", s)
print("500 -", p)
print("200 -", i)
print("100 -", d)
print("50 -", e)
print("20 -", r)
print("10 -", m)
print("5 -", a)
print("1 -", n)

# int(), eval(), type()











