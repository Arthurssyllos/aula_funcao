 #Primeiro passo: criar a função

def ano_bi(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True

 #Segundo passo: criar listas, 2° lista com valores booleanos

dados_teste = [1900, 2000, 2016, 1987,2020]

resultados_reais = [False, True, True, False, True]

 #Terceiro passo: criar um loop, que: 'para i em tanto (len(dados_teste)):
                                                    #  |_ > len para ler a lista
 # yr ele atribuiu que é igual a lista de dados_teste porém com o valor de i
 # ele vai printar dentro do loop uma seta ( - > ) com end=" " (espaço)
 # cria uma variável result que é igual a ano_bi (função) + yr

for i in range(len(dados_teste)):
    yr = dados_teste[i]
    print(yr, '->', end=" ")
    result = ano_bi(yr)
    if result == resultados_reais[i]:
        print('OK')
    else:
        print('Falha')