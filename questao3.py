numero = int(input("Digite um número inteiro:"))
mensagem = f"O número {numero} "

if numero % 15 == 0:
    mensagem += "é divisível por 3 e por 5."
elif numero % 3 == 0:
    mensagem += "é divisível por 3"
elif numero % 5 == 0:
    mensagem += "é divisível por 5"
else:
    mensagem += "não é divisível por 3 e nem por 5 "

print(mensagem)