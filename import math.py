# Variancia 
numeros = [10, 7, 8, 9, 6]
qte = len(numeros)
media = sum(numeros) / qte
soma_quadrado = 0
for number in numeros:
  soma_quadrado += (number - media) ** 2
variancia = soma_quadrado / qte
print(variancia)