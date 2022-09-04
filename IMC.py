import math
altura = float(input("Altura em centímetros: "))
altura = (altura / 100) #Modifica a altura em cm para m
peso = float(input("peso em kg: "))
imc = (peso / (math.pow(altura, 2)))
print(f'IMC = {imc:.1f}', "kg/m²") #Mostra o IMC em 1 casa decimal

