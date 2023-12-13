'''A função converteString possui um parâmetro  chamado caractere, com um valor  "palavra".'''
def converteString(caractere = "palavra"): 
    '''Dentro da função, há um bloco try-except. '''
    try: 
        converter = float(caractere) #  tenta converter o valor do parâmetro caractere em um número de ponto flutuante usando float(caractere)'''
        print('String convertida em float com sucesso !',converter)
        '''Se a conversão for bem-sucedida, ou seja, se o valor puder ser convertido para um float, o programa imprime uma mensagem indicando que a conversão foi feita com sucesso, juntamente com o valor convertido'''
    except ValueError : # Se ocorrer um erro durante a conversão, especificamente um ValueError, o código dentro do bloco except será executado. Nesse caso, ele imprime uma mensagem informando que houve um erro ao tentar converter a string em um float.
        print("Erro ao converter a string em float")
        
converteString() #chama a função

    