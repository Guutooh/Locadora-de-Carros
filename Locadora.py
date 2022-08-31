import os

carros = [
    ('Chevrolet Tracker', 120),
    ('Chevrolet Onix', 90),
    ('Chevrolet Spin', 150),
    ('Hyundai HB20', 85),
    ('Hyundai Tucson', 120),
    ('Fiat Uno', 60),
    ('Fiat Mobi', 70),
    ('Fiat Pulse', 130)
]
alugados = []


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(f'[{i}] {car[0]} - R$ {car[1]} /dia.')


while True:
    print('=========')
    print('Bem vindo à locadora de carros! ')
    print('=========')
    print('O que deseja fazer? ')
    op = int(input('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro \n'))

    os.system('cls')
    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print('==========')
        codCar = int(input('Escolha o código do carro: '))
        dias = int(input('Por quantos dias você deseja alugar este carro? '))
        os.system('cls')

        print(f'Você escolheu {carros[codCar][0]} por {dias} dias.')
        print(f'O aluguel totalizaria R$ {dias * carros[codCar][1]:.2f} - Deseja alugar? ')

        conf = int(input("0 - Sim | 1 - Não "))
        if conf == 0:
            print(f'Parabéns você alugou o {carros[codCar][0]} por {dias} dias.')
            alugados.append(carros.pop(codCar))

    elif op == 2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue a lista de carros alugados. Qual você deseja devolver? ')
            mostrar_lista_de_carros(alugados)
            print("")
            cod = int(input('Escolha o código do carro que deseja devolver: '))
            if conf == 0:
                print(f'Obrigado por devolver o carro {alugados[cod][0]}')
                carros.append(alugados.pop(cod))

    print('===========')
    print('0 - Continuar | 1 - Sair ')
    print('===========')
    if int(input()) == 1:
        print('Obrigado.')
        break
