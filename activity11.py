#import demo
import getpass

username = "sushimegumi"
password = "chimerashadowgarden"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")

if u == username or p == password:
	print("username and password")

else:
	print("access denied")