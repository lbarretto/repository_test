palavra = input("Digite uma palavra: ").strip().lower()

# Inverte a string utilizando fatiamento (slicing [::-1])
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo. Invertida fica: '{palavra_invertida}'")