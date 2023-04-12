import phonenumbers
from phonenumbers import geocoder

while True:

    phone = input('Digite o número do telefone no formato como exemplo +55(11)988000000: ')

    phone_number = phonenumbers.parse(phone)

    print(geocoder.description_for_number(phone_number, 'pt'))

    encerrar = int(input('''Deseja encerrar o programa?
1)sim
2)não
'''))
    if encerrar == 1:
        break