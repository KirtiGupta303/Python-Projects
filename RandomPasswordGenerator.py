import random
import string

pass_len = int(input("Enter length of password to generate: "))
charValues = string.ascii_letters + string.digits + string.punctuation

#using list comprehension [function for i in range(n)]
password = "".join([random.choice(charValues) for i in range(pass_len)])

#using for loop 
# password = ""
# for i in range(pass_len):
#     password +=random.choice(charValues)

print("Your random password is :",password)