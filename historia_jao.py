from time import sleep
from cores import colors
from maquina import type_writer
class Node:
    def __init__(self, question=None, left=None, right=None, final=False):
        self.question = question
        self.left = left
        self.right = right
        self.final = final

class BinaryTree:
    def __init__(self, root=None):
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
                    if "Você acusa Eloy Casapequena, por que sim" in node.left.question:
                        print(colors.LIGHTCYAN+"Parabéns! Você resolveu o caso! Eloy estava manipulando o filho do lorde."+colors.END)
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
                        print(colors.GREEN+"E você descobre que há falta de registros da sua presença no dia do crime." +colors.END)
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

def jogar2():
    print("\n---------------------------------------------------------------------------------\n")
    sleep(0.2)
    #aqui começa o contexto inicial
    mensagem =colors.GREEN+ "> VOCÊ CHEGOU AO NÍVEL 4! <\n"
    type_writer(mensagem)
    mensagem1 =colors.RED + "Obs: se errar a acusação, volta para o inicio do jogo. \n"
    type_writer(mensagem1)
    sleep(0.2)
    mensagem11 =colors.RED + "-- O culpado é quem você menos espera -- \n"
    type_writer(mensagem11)
    sleep(0.2)
    mensagem2 =colors.GREEN + "\n Dias após os acontecimentos anteriores\n"
    type_writer(mensagem2)
    sleep(0.2)
    mensagem3 =colors.GREEN+ "após um melhor depoimento de Sarah Blackwood  \n"+ colors.END
    type_writer(mensagem3)
    sleep(0.2)
    mensagem4 =colors.GREEN+ "ela não demonstrava nenhum indício de ter feito o crime \n"+ colors.END
    type_writer(mensagem4)
    sleep(0.2)
    mensagem5 =colors.GREEN+ "pois estava apaixonada pelo Dr. Jonathan Parker. \n"+ colors.END
    type_writer(mensagem5)
    sleep(0.2)
    mensagem6 =colors.GREEN+ "o que também inocentava o Dr. Jonathan Parker, pois estava planejando se casar com a mesma\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.GREEN+ "mas o Dr. Jonathan Parker revelou algo importante, um dos suspeitos estava mentindo \n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.GREEN+ "Victor! mas não era apenas isso, havia mais alguem Eloy Casapequena.\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.DARKRED+ "\nOs suspeitos:\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    #aqui termina o contexto inical
    #aqui começa a descrição dos suspeitos
    print(colors.CYAN + "1. Eloy Casapequena: Um musico qualquer não parece ter muitas ambições.")
    sleep(0.2)
    print("2. Victor Blackwood: Filho com desavenças sobre os negócios da família e acesso à mansão.")
    sleep(0.2)
  
    #aqui termina a descrição dos suspeitos
    mensagem7 = colors.BLUE + "\nSua missão é coletar pistas, interrogar os suspeitos e resolver o caso.\n"
    type_writer(mensagem7)
    sleep(0.2)
    mensagem8 = "Vamos começar!\n" + colors.END
    type_writer(mensagem8)
    sleep(0.2)
    print("\n---------------------------------------------------------------------------------\n")

    arvore = BinaryTree()

    root = arvore.add(colors.YELLOW + "Você está no local do crime. O que você faz?" + colors.END,
                      colors.GREEN + "Você decide acusar alguém." + colors.END,
                      colors.GREEN + "Você decide analisar melhor a reação dos novos suspeitos." + colors.END)

    root.left.left = Node(colors.BLUE+ "Você acusa o filho, Victor Blackwood."+colors.END, final=True)
    root.left.right = Node(colors.BLUE+"Você acusa o musico, Eloy Casapequena."+colors.END, final=True)

    root.right.left = arvore.add("Victor Blackwood, demonstrava medo.",
                                 "Você o questiona.",
                                 "Você continua procurando mais informações.")

    root.right.right = arvore.add("Eloy, parecia bem calmo afinal era apenas um musico qualquer.",
                                  "Você decide perguntar mais sobre a musica.",
                                  "Você continua procurando mais informações.")

    root.right.left.left = Node("Você decide acusar o Victor Blackwood", final=True)
    root.right.left.right = arvore.add("Você questioná-la sobre sua reação.",
                                       "Você decide acusar alguém com base no depoimento da testemunha.",
                                       "Você continua procurando mais informações.")

    root.right.right.left = Node("Você acusa o musico, Eloy Casapequena", final=True)
    root.right.right.right = arvore.add("Você endaga o musico sobre sua relação com victor.",
                                        "Você decide acusar alguém com base no objeto.",
                                        "Você continua procurando mais informações.")

    root.right.left.right.left = Node("Você acusa Victor Blackwood, por demonstrar tanto medo.", final=True)
    root.right.left.right.right = Node("Com certeza é o Victor", final=True)

    root.right.right.right.left = Node("Você acusa Eloy Casapequena, por que sim", final=True)
    root.right.right.right.right = Node("volte ao inicio", final=True)

    arvore.root = root

    arvore.traverse(arvore.root)

#jogar2()
