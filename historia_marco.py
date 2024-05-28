from time import sleep
from cores import colors
from maquina import type_writer
class Node:
    def _init_(self, question=None, left=None, right=None, final=False):
        self.question = question
        self.left = left
        self.right = right
        self.final = final

class BinaryTree:
    def _init_(self, root=None):
        self.root = root

    def add(self, question, left_question=None, right_question=None, final_left=False, final_right=False):
        new_node = Node(question)
        new_node.left = Node(left_question, final=final_left) if left_question else None
        new_node.right = Node(right_question, final=final_right) if right_question else None
        return new_node

    def traverse(self, node):
        if node:
            questao = colors.YELLOW+node.question+"\n"+colors.END
            type_writer(questao)
            sleep(0.2)
            if node.left and node.left.question:
                sleep(0.2)
                print(colors.LIGHTPURPLE+"1:"+colors.END,colors.random_color() + node.left.question+colors.END)
            if node.right and node.right.question:
                sleep(0.2)
                print(colors.LIGHTPURPLE+"2:"+colors.END,colors.random_color() + node.right.question+colors.END)
            sleep(0.2)
            choice = input(colors.DARKCYAN + "Escolha [1/2]: -> " + colors.END)
            print("\n---------------------------------------------------------------------------------\n")
            if choice == "1" and node.left:
                if node.left.final:
                    print(node.left.question)
                    if "resolve o caso" in node.left.question:
                        print(colors.LIGHTCYAN+"Parabéns! Você resolveu o caso!"+colors.END)
                    else:
                        print(colors.LIGHTRED+"Não há provas suficientes. Voltando ao início da fase...\n"+colors.END)
                        sleep(3)
                        print("\n---------------------------------------------------------------------------------\n")
                        self.traverse(self.root)
                else:
                    self.traverse(node.left)
            elif choice == "2" and node.right:
                if node.right.final:
                    print(node.right.question)
                    if "Você decide continuar investigando." in node.right.question:
                        print(colors.GREEN+"E descobre que na verdade sempre houve esforço e proteção da sua parte em relação ao Lorde" +colors.END)
                    else:
                        print(colors.LIGHTRED+"Não há provas suficientes. Voltando ao início da Fase...\n"+colors.END)
                        sleep(3)
                        print("\n---------------------------------------------------------------------------------\n")
                        self.traverse(self.root)
                else:
                    self.traverse(node.right)
            else:
                print(colors.RED+"Opção inválida. Por favor, escolha '1' ou '2'."+colors.END)
                self.traverse(node)
        else:
            print("Fim do jogo.")

def iniciar_jogo():
    print("\n---------------------------------------------------------------------------------\n")
    sleep(0.2)
    #aqui começa o contexto inicial
    mensagem =colors.GREEN+ "> VOCÊ CHEGOU AO NÍVEL 3! <\n"
    type_writer(mensagem)
    mensagem1 =colors.RED + "Obs: se errar a acusação, volta para o inicio do jogo. \n"
    type_writer(mensagem1)
    sleep(0.2)
    mensagem11 =colors.RED + "-- O culpado é quem você menos espera -- \n"
    type_writer(mensagem11)
    sleep(0.2)
    mensagem =colors.GREEN+ "\nDias após o início da investigação, Arthur Blake descobre duas novas peças no quebra-cabeça: \n"
    type_writer(mensagem)
    sleep(0.2)
    mensagem2 = "Sarah Blackwood, uma filha ilegítima de Lorde Blackwood, e o Dr. Jonathan Parker, médico da família.\n"
    type_writer(mensagem2)
    sleep(0.2)
    mensagem22 = "E percebe que há mais membros bem próximos ao Lorde que também não tinham registros de presença\n"
    type_writer(mensagem22)
    sleep(0.2)
    mensagem222 = "no momento do crime, descartando assim a exclusividade de suspeitas sobre Tyler e Alice.\n"
    type_writer(mensagem222)
    sleep(0.2)
    mensagem3 = "Essas revelações lançam luz sobre possíveis motivos e conexões obscuras dentro da família. Sarah surge \n"
    type_writer(mensagem3)
    sleep(0.2)
    mensagem6 = "como uma figura enigmática, enquanto o acesso ilimitado de Dr. Parker à mansão o coloca sob \n"
    type_writer(mensagem6)
    sleep(0.2)
    mensagem66 = "suspeita. Com o número de suspeitos aumentando, Arthur se vê imerso em um labirinto de intrigas familiares, \n"
    type_writer(mensagem66)
    sleep(0.2)
    mensagem67 = "onde cada nova descoberta revela mais sobre os segredos sombrios que cercam o assassinato de Lorde Blackwood.\n"+ colors.END
    type_writer(mensagem67)
    sleep(0.2)

    mensagem6 =colors.DARKRED+ "\nOs suspeitos até então são:\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    #aqui termina o contexto inical
    #aqui começa a descrição dos suspeitos
    print(colors.CYAN + "1. Lydia Raven: Prima distante com interesse no ocultismo e presença noturna frequente.")
    sleep(0.2)
    print("2. Tyler Thompson: Mordomo leal com conhecimento íntimo da rotina da vítima e possível motivo pessoal.")
    sleep(0.2)
    print("3. Sarah Blackwood: Filha ilegítima de Lorde Blackwood, infiltrada na mansão como governanta. ")
    sleep(0.2)
    print("4. Dr. Jonathan Parker: Médico da família e amigo íntimo de Lorde Blackwood. " + colors.END)
    sleep(0.2)
    #aqui termina a descrição dos suspeitos
    mensagem7 = colors.BLUE + "\nSua missão é coletar pistas, interrogar os suspeitos e resolver o caso.\n"
    type_writer(mensagem7)
    sleep(0.2)
    mensagem8 = "Vamos lá!\n" + colors.END
    type_writer(mensagem8)
    sleep(0.2)
    print("\n---------------------------------------------------------------------------------\n")

    arvore = BinaryTree()

    root = arvore.add(colors.YELLOW + "Você está no local do crime. O que você faz?" + colors.END,
                      colors.GREEN + "Você decide acusar alguém." + colors.END,
                      colors.GREEN + "Você decide analisar melhor os novos suspeitos." + colors.END)

    root.left.left = Node(colors.BLUE+ "Você acusa Sarah Blackwood, a filha ilegítima."+colors.END, final=True)
    root.left.right = Node(colors.BLUE+"Dr. Jonathan Parker, o médico da família."+colors.END, final=True)

    root.right.left = arvore.add("Sarah Blackwood, sofre severamente por sua rejeição como filha.",
                                 "Você decide acusar alguém com base na pegada.",
                                 "Você continua procurando mais informações.")

    root.right.right = arvore.add("Dr. Jonathan Parker, foi citado no testamento do Lorde.",
                                  "Você decide acusar alguém baseado no álibi.",
                                  "Você continua procurando mais informações.")

    root.right.left.left = Node("Você decide acusar Sarah Blackwood, a filha ilegítima.", final=True)
    root.right.left.right = arvore.add("Você questioná-la sobre sua história.",
                                       "Você decide acusar alguém com base no depoimento da testemunha.",
                                       "Você continua procurando mais informações.")

    root.right.right.left = Node("Você acusa o Dr. Jonathan Parker, o médico da família.", final=True)
    root.right.right.right = arvore.add("Você questiona o médico sobre estar no testamento da vítima.",
                                        "Você decide acusar alguém com base no objeto.",
                                        "Você continua procurando mais informações.")

    root.right.left.right.left = Node("Você acusa Sarah Blackwood, por ter enfatizado sede de vingança.", final=True)
    root.right.left.right.right = Node("Você decide continuar investigando.", final=True)

    root.right.right.right.left = Node("Você acusa o Dr. Jonathan Parker por contradição na explicação.", final=True)
    root.right.right.right.right = Node("Você decide continuar investigando.", final=True)

    arvore.root = root

    arvore.traverse(arvore.root)

#iniciar_jogo()