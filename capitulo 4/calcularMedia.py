# A função calcular_media possui três parâmetros opcionais (portugues, matematica e ingles) com  os valores os 7, 6.8 e 9
def calcular_media(portugues = 7, matematica = 6.8, ingles = 9):
    # Calcula a média das três disciplinas
    media = (portugues + matematica + ingles) /3
    
    # Imprime a média com duas casas decimais
    print(f'Sua media foi de {media:.2}')
    
    #  verifica se a média é maior ou igual a 6 e imprime uma mensagem correspondente informando se o aluno foi aprovado ou não.
    if media >= 6:
        print("Parabéns ! você foi aprovado")
        
    else:
        print("Lamento! Mas você não passaou de ano")
        
 # Chama a função sem passar nenhum argumento
calcular_media()
