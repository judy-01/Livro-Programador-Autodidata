inforPessoal = {}
inforPessoal['nome'] = input("Qual é o seu nome completo ?")
inforPessoal['endereço'] = input("Qual o seu endereço ? ")
inforPessoal['telefone'] =int(input('Telefone para contato ?'))
inforPessoal['email']=  input('Qual é o seu melhor email ? ')

print("\nInformações do usuário\n")
for chave, valor in inforPessoal.items():
    print(f'{chave}: {valor}')