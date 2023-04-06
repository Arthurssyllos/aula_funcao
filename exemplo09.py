def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


notas = [7.5, 8.0, 6.5, 9.0]
media = calcular_media(notas)

print('Seja bem vindo! Ao sistema de calcular média de notas, em que as notas são:\n', notas)

print('Agora vamos calcular a média!')

print('A média é:', media)

