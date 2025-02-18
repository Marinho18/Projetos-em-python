n1 = int(input(f"digite um numero: "))
n2 = int(input(f"digite outro numero: "))

soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2

if n2 != 0:
    divisao = n1/n2
    print(f"Divisão é: {divisao:.2f}")
else:
    divisao = "Indefinida"
    print("ERRO: Divisão por zero não é permitida")

print(f"soma é: {soma}")
print(f"subtração é: {subtracao}")
print(f"multiplicação é: {multiplicacao}")
print(f"divisão é: {divisao}")

