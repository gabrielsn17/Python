import random
import string

tamanho = int(input('Digite o número de caracteres que deseja em sua senha: '))

chars = string.ascii_letters + string.digits + '@#$%¨&*()_-=+;:,<>[]{}/\|'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))