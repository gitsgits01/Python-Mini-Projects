#Random Password Generator

import random #random module
import string #string module
password_len = 12 #password length
charValues = string.ascii_letters + string.digits + string.punctuation
password= ""
for i in range(password_len):
    password += random.choice(charValues)
print("Your random password is:", password)