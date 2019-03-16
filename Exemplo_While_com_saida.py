resposta=""

qtde_sim=0
qtde_nao=0

while (resposta!="SIM"):
    is_trabalha=""
    while is_trabalha!="SIM" and is_trabalha!="NAO":
        is_trabalha=input ("Você trabalha (SIM ou NAO)? ").upper()
    if is_trabalha=="SIM":
        qtde_sim+=1
    else:
        qtde_nao+=1
    resposta=input("Deseja sair? ").upper()
print("Resultado")
print("Total de pessoas que trabalham.....:", qtde_sim)
print("Total de pessoas que não trabalham..:", qtde_nao)
