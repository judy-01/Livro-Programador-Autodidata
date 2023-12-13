
#Esta função recebe um número  com o valor  8 e retorna o resultado da divisão inteira desse número por 2.
def dividirPor2( numero = 8): 
    return numero // 2  

#Esta função recebe um número com o valor  3 e retorna o resultado da multiplicação desse número por 4.
def multiplicarPor4( numero = 3):
    return numero * 4  


resultadoDivisao = dividirPor2(10) # Chama a função dividirPor2 com o argumento 10 e armazena o resultado (5, pois 10 dividido por 2 é igual a 5) na variável resultadoDivisao.
resultadoMultiplicacao = multiplicarPor4 (7)  #  Chama a função multiplicarPor4 com o argumento 7 e armazena o resultado (28, pois 7 multiplicado por 4 é igual a 28) na variável resultadoMultiplicacao. 

#Imprime o resultado final, que é o resultado da multiplicação por 4 do resultado da divisão por 2. Neste caso, resultadoDivisao é 5, então multiplicarPor4(resultadoDivisao) resulta em 20 (5 multiplicado por 4), e essa é a saída final impressa.
print(f'Resultado final : {multiplicarPor4(resultadoDivisao)}') 