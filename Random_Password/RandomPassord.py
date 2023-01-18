import string
import random

characters = list(string.ascii_letters + string.digits +"!@£$%&*^()#.,")
password_length = int(input("how long should the password be?"))

random.shuffle(characters)
password = []

for x in range(password_length):
    password.append(random.choice(characters))
password = "".join(password)
print(str(password))