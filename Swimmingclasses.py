nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade <8:
    print("olá,", nome, "você não óde participar das aulas de natação.")
elif idade >=8 and idade <=12:
    print("olá,", nome, "A participação das aulas de natação é opcional para você.")
else:
    print("olá,", nome, "A participação das aulas de natação é obrigatória para você.")
    
