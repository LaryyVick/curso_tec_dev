#----------- OPERADOR AND -------------------------

# idade = int(input("Qual é a sua idade? "))
# cnh = input("Tem CNH? (sim/Não): ")

# if idade >= 18 and cnh == "sim":
#     print ("Você pode dirigir")
# else:
#     print("Não pode dirigir")

# ----------- OPERADOR OR ------------------------

estudante = input("Você é estudante (sim/não)? ")
idoso = input("Você é Idoso (sim/não)? ")

if estudante == "sim" or idoso == "sim":
    print("Você ganhou desconto!")
else:
    print("Você não ganhou desconto")
