numeros = [12,56,2, 7, 10, 8, 5]
while True :
    entrada = input ('Digite um número ou X para sair '.upper())
    if entrada =="X":
        break
    
    try :
        palpite = int(entrada)
        if palpite in numeros:
            print("Palpite correto")
        else:
            print("Palpite errado")
    except ValueError :
        print("Entrada inválida, por favor digite um número ou X para sair")