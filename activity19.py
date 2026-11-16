from getpass import getpass
isLogin = False
loginAttempts = 0

u = "Spidey"
p= "canyougetmehome?"

while isLogin == False:
    u = input("Enter your username ---> ")
    p = getpass("Enter your password ---> ")

    if uname == u and pword == p:
        print("Login successful!")
        print("Total Login Attempts: ", loginAttempts)
        isLogin = True
    else:
        print("Login failed! Please try again.")
        loginAttempts += 1
        isLogin = False