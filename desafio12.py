produto=float(input("Qual o preço do produto? "))
res=produto*0.05
preco=produto-res
print(f"O produto custava {produto} na promoção com desconto de 5% vai custar {preco:.2f}")