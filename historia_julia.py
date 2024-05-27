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
                    if "resolve o caso" in node.left.question:
                        print(colors.LIGHTCYAN+"Parabéns! Você resolveu o caso!"+colors.END)
                    else:
                        print(colors.LIGHTRED+"Não há provas suficientes. Voltando ao início do jogo...\n"+colors.END)
                        sleep(3)
                        print("\n---------------------------------------------------------------------------------\n")
                        self.traverse(self.root)
                else:
                    self.traverse(node.left)
            elif choice == "2" and node.right:
                if node.right.final:
                    print(node.right.question)
                    if "resolve o caso" in node.right.question:
                        print("Parabéns! Você resolveu o caso!")
                    else:
                        print(colors.LIGHTRED+"Não há provas suficientes. Voltando ao início do jogo...\n"+colors.END)
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
    mensagem =colors.GREEN+ "BEM-VINDO AO JOGO DE DETETIVE!\n"
    type_writer(mensagem)
    mensagem1 =colors.RED + "Obs: se errar a acusação, volta para o inicio do jogo. \n"
    type_writer(mensagem1)
    sleep(0.2)
    mensagem2 =colors.GREEN + "\nEm uma pequena e sombria vila chamada Ravenwood, conhecida por suas florestas densas e neblina constante, \n"
    type_writer(mensagem2)
    sleep(0.2)
    mensagem3 =colors.GREEN+ "você, Arthur Blake, um famoso detetive, reside. Natural de uma cidade vizinha, você foi chamado para\n"+ colors.END
    type_writer(mensagem3)
    sleep(0.2)
    mensagem4 =colors.GREEN+ "resolver um caso perturbador que abalou os moradores locais. O corpo de Lorde Henry Blackwood, \n"+ colors.END
    type_writer(mensagem4)
    sleep(0.2)
    mensagem5 =colors.GREEN+ "o patriarca de uma das famílias mais influentes da vila, foi encontrado em sua mansão isolada,\n"+ colors.END
    type_writer(mensagem5)
    sleep(0.2)
    mensagem6 =colors.GREEN+ "e as circunstâncias em torno de sua morte são misteriosas. Ao chegar em Ravenwood em uma\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.GREEN + "uma noite chuvosa, você é recebido pelo som inquietante das árvores ao vento, onde a atmosfera é carregada\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.GREEN + "de tensão.Lá está a mansão Blackwood, com sua arquitetura gótica e sombria, que é o cenário perfeito\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.DARKRED+ "para um mistério de assassinato. Os habitantes da vila, embora desconfiados de estranhos,\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.DARKRED+ "esperam ansiosamente que você resolva o caso e traga paz à sua comunidade.\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)
    mensagem6 =colors.DARKRED+ "\n Os possíveis suspeitos são:\n"+ colors.END
    type_writer(mensagem6)
    sleep(0.2)


    
    #aqui termina o contexto inical
    #aqui começa a descrição dos suspeitos
    print(colors.CYAN + "1. Alice Blackwood: Viúva com acesso à mansão e possíveis conflitos conjugais e financeiros.")
    sleep(0.2)
    print("2. Victor Blackwood: Filho com desavenças sobre os negócios da família e acesso à mansão." + colors.END)
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
                      colors.GREEN + "Você decide procurar mais informações." + colors.END)

    root.left.left = Node(colors.BLUE+ "Você acusa a viúva,  Alice Blackwood."+colors.END, final=True)
    root.left.right = Node(colors.BLUE+"Você acusa o filho, Victor Blackwood"+colors.END, final=True)

    root.right.left = arvore.add("Você encontra uma pista importante: uma pegada de sapato.",
                                 "Você decide acusar alguém com base na pegada.",
                                 "Você continua procurando mais informações.")

    root.right.right = arvore.add("Você encontra um álibi que descarta um dos suspeitos.",
                                  "Você decide acusar alguém baseado no álibi.",
                                  "Você continua procurando mais informações.")

    root.right.left.left = Node("Você pode  acusa a esposa com base na pegada, mas não há provas suficientes.", final=True)
    root.right.left.right = arvore.add("Você continua procurando e encontra uma testemunha.",
                                       "Você decide acusar alguém com base no depoimento da testemunha.",
                                       "Você continua procurando mais informações.")

    root.right.right.left = Node("Você acusa o sócio com base no álibi, mas não há provas suficientes. Tente novamente.", final=True)
    root.right.right.right = arvore.add("Você encontra um objeto pessoal do suspeito.",
                                        "Você decide acusar alguém com base no objeto.",
                                        "Você continua procurando mais informações.")

    root.right.left.right.left = Node("Você acusa a esposa com base no depoimento, mas não há provas suficientes. Tente novamente.", final=True)
    root.right.left.right.right = Node("Você encontra a arma do crime com impressões digitais do jardineiro, inocentando os outros. Você resolve o caso!", final=True)

    root.right.right.right.left = Node("Você acusa o sócio com base no objeto, mas não há provas suficientes. Tente novamente.", final=True)
    root.right.right.right.right = Node("Você encontra um novo suspeito com um motivo forte, inocentando os outros. Você resolve o caso!", final=True)

    arvore.root = root

    arvore.traverse(arvore.root)

iniciar_jogo()
