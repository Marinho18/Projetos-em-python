nota1 = float(input(f"coloque ai sua primeira nota:"))
nota2 = float(input(f"agora sua segunda nota:  "))
nota3 = float(input(f"agora a terceira nota: "))

media = (nota1 + nota2 + nota3) /3

if media >= 7:
    status = "Aprovado"
elif 5 <= media < 7:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f"Sua média foi: {media:2f}")
print(f"Status: {status}")
