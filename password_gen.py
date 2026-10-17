import random
import string
def generate_password(length=12):
       characters = string.ascii_letters + string.digits + "!@#$%^&*"
       password = "".join(random.choice(characters) for i in range(length))
       return password
my_password = generate_password(16)
print("为你生成的密码强度是：",my_password)