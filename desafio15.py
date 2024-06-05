dias=int(input('Quantos dias alugados? '))
km=int(input('Quantos km percorridos? '))
carro=dias*60
rodado=km*0.15
res=carro+rodado
print(f'O total a pagar é de R${res}')
