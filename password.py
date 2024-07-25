import random
import string

special_characters = "!@#$"
def gerar_senha():
    tamanho_senha = 14
    caracteres_permitidos = string.ascii_letters + string.digits + special_characters

    senha = ''.join(random.choice(caracteres_permitidos) for _ in range(tamanho_senha))
    return senha

senha_aleatoria = gerar_senha()
print("Password:", senha_aleatoria)