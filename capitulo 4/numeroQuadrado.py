
def num():
    numero = int(input("Digite um número :")) # Solicita ao usuário que digite um número. A função input() captura a entrada do usuário como uma string, e int() converte essa string em um número inteiro (int) antes de atribuí-lo à variável numero.
    print(f'{numero} ao quadrado é {numero ** 2}') #Calcula o quadrado do número inserido pelo usuário e imprime uma mensagem indicando o número inserido e seu quadrado.
num() # Chama a função num(), que realiza o processo descrito acima quando é executada.

# outras formas de resolver o mesmo problema acima :
'''
------------------------------------
num=int(input("Digite um numero :"))
def numQua():
    return num **2    
print(f'{num} ao quadrado é ',numQua())

---------------------------------
def n():
   return 6 **2
print(n())

-----------------------------------
def x(a = 7):
   a **2
   print(a)
x()
'''