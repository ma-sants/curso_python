try:
   num=int(input("digite um número: ")) 
   print(num)

except:
   print("digite um valor válido.")

   #try e except são usados para mostrar uma mensagem bonitinha quando dar erro. Se não der erro tudo ocorre normalmente.#

finally: 
   print("sempre executa")

   #finally independente do que aconteça ele sempre executa.#