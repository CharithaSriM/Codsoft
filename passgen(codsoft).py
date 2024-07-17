import random
print("\t\tLET'S GENERATE RANDOM PASSWORD")
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
length=int(input("Enter desired length of the password : "))
password=[]
for x in range(length):
    password.append(random.choice(letters))
newPassword=" ".join(password)
print("Password generated is",newPassword)
