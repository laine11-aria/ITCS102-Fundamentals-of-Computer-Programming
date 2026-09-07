#basic if else program 

username = "sushimegumi"
password = "chimerashadowgarden"

u = input("Input USERNAME ---> ")
p = input("Input PASSWORD ---> ")

if u == username or p == password:
	print("username and password")

else:
	print("access denied")