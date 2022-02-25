from random import randint


def str_validar(txt):
    ok = False
    valido = 0
    while True:
        valido = str(input(txt))
        if valido.isalpha():
            ok = True
        else:
            print('\033[1;31mDigite apenas letrar...\033[m')
        if ok:
            break
    return valido


while True:
    giro_dado = str_validar('Você quer jogar o dado [S/N]: ').strip().upper()[0]
    dado = randint(0, 6)

    if giro_dado == 'S':
        print(dado)

    if giro_dado == 'N':
        break

print('-=' * 20)
print('Programa Encerrado.')
