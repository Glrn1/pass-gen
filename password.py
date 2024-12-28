import random
import string

special_characters = "!@#$"

def gen_pass():
    tamanho_senha = 14
    chars = string.ascii_letters + string.digits + special_characters

    password = ''.join(random.choice(chars) for _ in range(tamanho_senha))
    return password

random_pass = gen_pass()
print("Password:", random_pass)
