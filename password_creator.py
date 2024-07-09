import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password_length = random.randint(8, 16)
    password = ''.join(random.sample(chars,password_length))

    while not any(char.isupper() for char in password) \
    or not any(char.islower() for char in password) \
    or not any(char in string.punctuation for char in password):
        password = ''.join(random.sample(chars, password_length))

    return password

password = generate_password     
print(password) 