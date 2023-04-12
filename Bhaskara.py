import math

def calculate_delta():
    delta = b**2-4*a*c
    return delta

def bhaskara1():
    x1 = (-b + math.sqrt(calculate_delta())) / (2*a)
    return x1

def bhaskara2():
    x2 = (-b - math.sqrt(calculate_delta())) / (2*a)
    return x2

a = float(input('Digiteo valor de "a": '))
if a == 0:
    print('Sendo "a" = 0, esta não é uma equação do segundo grau.')
    exit()
b = float(input('Digiteo valor de "b": '))
c = float(input('Digiteo valor de "c": '))

if calculate_delta() < 0:
    print('A equação não possui raízes reais pois o valor de delta é negativo')
elif calculate_delta() == 0:
    print('Delta igual a zero, a equação possui apenas uma raíz: %.2f'%bhaskara1())
elif calculate_delta() > 0:
    print("Duas raízes encontradas. São elas x' = %.2f e x'' = %.2f"%(bhaskara1(),bhaskara2()))