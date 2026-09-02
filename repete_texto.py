texto = input("Digite um texto: ")
vezes = int(input("Digite a quantidade de repetições: "))

# Multiplicação de string repete o texto
resultado = (texto + " ") * vezes

print("Texto repetido:", resultado.strip())