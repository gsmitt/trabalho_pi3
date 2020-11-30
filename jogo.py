import random as ran
import time
from termcolor import colored
from npcs import Npc
from eventos import Evento

# Definir status base

dinheiro = 5
povo = 5
exercito = 5
clero = 5

# Eventos (descricao,dinheiro,povo,exercito,clero,resultado)

# Descrição evento 1

desc1 = "Após a tempestade de ontem, goteiras surgiram no teto da igreja e precisa de reparos urgentemente, o padre perguntou se você pode ajudar com o dinheiro? "
din1 = -2
pov1 = 1
exe1 = 0
cle1 = +2
res1 = " Graças à sua ajuda a igreja foi consertada sem nenhum problema ou dificuldade. "

ev1 = Evento(desc1, din1, pov1, exe1, cle1, res1)

# Descrição evento 2

desc2 = "Ladrões estão invadindo o banco, devemos mandar nosso exército?"
din2 = +2
pov2 = 0
exe2 = -1
cle2 = 0
res2 = "Encontraram eles fugindo das fronteiras do reino, gracas à Deus pegamos eles e o dinheiro de volta."

ev2 = Evento(desc2, din2, pov2, exe2, cle2, res2)

# Descrição evento 3

desc3 = "O povo não esta indo à igreja, precisamos da ajuda do reino para icentivá-los."
din3 = +1
pov3 = -2
exe3 = 0
cle3 = +2
res3 = "Finalmente a frequência voltou ao normal."

ev3 = Evento(desc3, din3, pov3, exe3, cle3, res3)

# Descrição evento 4

desc4 = "Muitos de nossos soldados estão dizendo que você não é digno do reino, deseja que respondamos à estas críticas para você? "
din4 = +1
pov4 = 0
exe4 = -1
cle4 = 0
res4 = "Acho que eles entenderam o recado e não vão falar mais sobre você, pelo menos não da forma que não gostamos. "

ev4 = Evento(desc4, din4, pov4, exe4, cle4, res4)

# Descrição evento 5

desc5 = "Conseguimos ótimos alimentos, devemos dar ao povo? "
din5 = -1
pov5 = +2
exe5 = 0
cle5 = 0
res5 = "A população agradece os seus esforços e cantam seu nome em suas festas de comemoração. "

ev5 = Evento(desc5, din5, pov5, exe5, cle5, res5)

# Descrição evento 6

desc6 = "Estamos com pragas pela cidade, precisamos da ajuda do exército. "
din6 = -1
pov6 = +1
exe6 = -2
cle6 = 0
res6 = "Provavelmente impedimos o pior, obrigado pela ajuda. "

ev6 = Evento(desc6, din6, pov6, exe6, cle6, res6)

# Descrição evento 7

desc7 = "Devemos construir embaixadas perto dos outros reinos para evitar guerras. "
din7 = -2
pov7 = +1
exe7 = +1
cle7 = 0
res7 = "Acho que não teremos problemas por um bom tempo. "

ev7 = Evento(desc7, din7, pov7, exe7, cle7, res7)

# Descrição evento 8

desc8 = "Hà muitas pessoas para executar, preciso da ajuda do exército. "
din8 = 0
pov8 = -1
exe8 = +1
cle8 = 0
res8 = "Graças à isso tem mais espaço nas cadeias. "

ev8 = Evento(desc8, din8, pov8, exe8, cle8, res8)

# Descrição evento 9

desc9 = "O reino esta ficando sujo, precisamos de dinheiro para limpa-lo. "
din9 = -1
pov9 = +1
exe9 = 0
cle9 = 0
res9 = "O reino esta bem melhor! "

ev9 = Evento(desc9, din9, pov9, exe9, cle9, res9)

# Descrição evento 10

desc10 = "Precisamos de um toque de recolher, hà muitos ladrões pela cidade. "
din10 = 0
pov10 = +1
exe10 = 0
cle10 = 0
res10 = "Da até para fazer um passeio a noite agora. "

ev10 = Evento(desc10, din10, pov10, exe10, cle10, res10)

# Descrição evento 11

desc11 = "Devemos construir uma estatua de Jesus no centro da cidade para relembrar de sua passagem pelas nossas terras. "
din11 = -2
pov11 = +1
exe11 = 0
cle11 = +2
res11 = "Ficou linda!"

ev11 = Evento(desc11, din11, pov11, exe11, cle11, res11)

# Descrição evento 12

desc12 = "Temos que investir mais no exército, está muito fraco. "
din12 = -2
pov12 = 0
exe12 = +2
cle12 = -1
res12 = "Sinto que podemos dominar o reino vizinho agora. "

ev12 = Evento(desc12, din12, pov12, exe12, cle12, res12)

# Descrição evento 13

desc13 = "Devemos aumentar os impostos? "
din13 = +2
pov13 = -1
exe13 = 0
cle13 = -1
res13 = "concordo com a sua recolha, estava muito baixo mesmo. "

ev13 = Evento(desc13, din13, pov13, exe13, cle13, res13)

# Descrição evento 14

desc14 = "Eu e meus companheiros das periferias estamos passando fome devido à seca. Imploramos por sua ajuda!"
din14 = -1
pov14 = +1
exe14 = 0
cle14 = 0
res14 = "Agora poderemos sobreviver, muito obrigado!"

ev14 = Evento(desc14, din14, pov14, exe14, cle14, res14)

# Npcs (nome,eventos)

padre = Npc("Padre", [ev1, ev3, ev9, ev11, ev10])
nobre = Npc("Nobre", [ev2, ev4, ev5, ev8, ev7, ev13])
soldado = Npc("Soldado", [ev2, ev9, ev7, ev10, ev12])
campones = Npc("Camponês", [ev5, ev6, ev9, ev11, ev14])
npcs = [padre, nobre, soldado, campones]

# Calendário (randomizador de data)

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
         "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
ano = ran.randint(500,1300)
m = ran.randint(0,(len(meses)-1))
s = 0

game = True

# Corpo do Jogo 
while game == True:
    s += 1
    score = [s // 12, s % 12]

    # Calendário (atualizador de data)
    mes = meses[m]
    
    print("")
    print("+-------------------------------------------------------------------------------------------------------------------------------+")
    print("")
    print(f"" + str(mes) + " de " + str(ano) + ".")
    
    m += 1
    if m > 11:
        m = 0
        ano += 1
    
    # Randomizador de eventos
    x = ran.randint(0,(len(npcs)-1))
    evento_atual = ran.choice(npcs[x].eventos)
    npc_atual = npcs[x].nome
    
    print("")
    print(f"Um " + colored(npc_atual, "yellow") + " vem à você.")
    print("")
    print(f"Ele lhe diz: " + evento_atual.descricao)
    print("")
    print("+-------------------------------------------------------------------------------------------------------------------------------+")
    print("")

    # delay
    time.sleep(0.5)

    dialogo = True
    
    while dialogo == True:
        print("Você aceita?")
        print("")
        print("+------------------+")
        print("1 - " + colored("Sim.", "green"))
        print("2 - " + colored("Não.", "red"))
        print("3 - Sair do jogo.")
        print("+------------------+")
        print("")
        aceitar_proposta = input("Sua resposta: ")
        
        if aceitar_proposta == "1":
            dinheiro += evento_atual.dinheiro
            povo += evento_atual.povo
            exercito += evento_atual.exercito
            clero += evento_atual.clero
            resultado = evento_atual.resultado
            dialogo = False
        elif aceitar_proposta == "2":
            resultado = "Nada acontece."
            dialogo = False
        elif aceitar_proposta == "3":
            resultado = ""
            game = False
            dialogo = False
        else:
            resultado = ""
            for i in range(0,25):
                print("")
            print("Escolha uma opção válida!")
            print("")
            print("")

    # delay
    time.sleep(0.5)

    if resultado != "":
        for i in range (0,25):
            print("")
        print(resultado)
        print("")
        print("")
        
    input("Aperte ENTER para continuar: ")

    for i in range (0,25):
        print("")
    
    # delay
    time.sleep(0.5)

    if game == True:
        print("+-----------------------------------------+")
        print("")
        print("A situação atual é:")
        print("")
        print(f"Dinheiro: " + colored(str(dinheiro), "yellow") + " Povo: " + colored(str(povo), "yellow") + " Exército: " + colored(str(exercito), "yellow") + " Clero: " + colored(str(clero), "yellow"))
        print("")
        print("+-----------------------------------------+")
        print("")
        input("Aperte ENTER para continuar: ")
    
    for i in range (0,25):
        print("")

    # Tela de fim de jogo 
    mostrar_score = (f"Você reinou por " + colored(score[0], "yellow") + " anos e " + colored(score[1], "yellow") + " meses.")
    bad_end = colored("Fim de Jogo", "red")
    
    if dinheiro < 0:
        print("O reino falíu, você foi raptado e vendido para um reino vizinho.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False

    elif dinheiro > 10:
        print("O reino ficou muito rico, decidiram que não precisam mais de um rei, você foi deposto.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False

    elif povo < 0:
        print("O povo ficou descontente, uma revolução se instaurou, você foi deposto.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False

    elif povo > 10:
        print("O povo ficou muito contente e não lhe teme mais, um rei sem influência já não é mais rei.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False
    
    elif exercito < 0:
        print("O exército ficou muito fraco e sucumbiu, seu reino foi invadido por uma nação inimiga.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False

    elif exercito > 10:
        print("O exército ficou muito forte e aplicou um golpe militar, você foi deposto.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False
    
    elif clero < 0:
        print("O clero perdeu seu poder e, com isso, sua influência sobre o povo, você foi deposto")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False
    
    elif clero > 10:
        print("O clero ficou muito influênte e tomou o controle do país.")
        print("")
        print(mostrar_score)
        print("")
        print("")
        input("Aperte ENTER para continuar: ")
        for i in range(0,25):
            print("")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print(bad_end)
        game = False

    time.sleep(1)
