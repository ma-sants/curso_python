import random 
nome1=input("Digite seu nome: ")
nome2=input("Digite seu nome: ")
nome3=input("Digite seu nome: ")
nome4=input("Digite seu nome: ")
alunos=(nome1,nome2,nome3,nome4)
res=random.choice(alunos)
print(f'O ganhador foi {res}')