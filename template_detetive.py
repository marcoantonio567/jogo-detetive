from time import sleep
from cores import colors

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
            print(node.question)
            sleep(0.5)
            if node.left and node.left.question:
                print("1:", node.left.question)
            if node.right and node.right.question:
                print("2:", node.right.question)
            choice = input(colors.DARKCYAN + "Escolha [1/2]: -> " + colors.END)
            print("\n---------------------------------------------------------------------------------\n")
            if choice == "1" and node.left:
                if node.left.final:
                    print(node.left.question)
                    if "resolve o caso" in node.left.question:
                        print("Parabéns! Você resolveu o caso!")
                    else:
                        print("Não há provas suficientes. Voltando ao início do jogo...")
                        self.traverse(self.root)
                else:
                    self.traverse(node.left)
            elif choice == "2" and node.right:
                if node.right.final:
                    print(node.right.question)
                    if "resolve o caso" in node.right.question:
                        print("Parabéns! Você resolveu o caso!")
                    else:
                        print("Não há provas suficientes. Voltando ao início do jogo...")
                        self.traverse(self.root)
                else:
                    self.traverse(node.right)
            else:
                print("Opção inválida. Por favor, escolha '1' ou '2'.")
                self.traverse(node)
        else:
            print("Fim do jogo.")

def iniciar_jogo():
    print("\n---------------------------------------------------------------------------------\n")
    print(colors.GREEN + "Bem-vindo ao jogo de detetive!")
    sleep(0.2)
    print("Você é um famoso detetive chamado ao local de um misterioso assassinato.")
    sleep(0.2)
    print("A vítima é um empresário rico encontrado morto em sua mansão. Há três suspeitos principais:" + colors.END)
    sleep(0.2)
    print(colors.RED + "1. A esposa da vítima, que tinha um relacionamento conturbado com ele.")
    sleep(0.2)
    print("2. O sócio da vítima, que estava em conflito devido a negócios.")
    sleep(0.2)
    print("3. O jardineiro, que foi demitido recentemente e estava insatisfeito." + colors.END)
    sleep(0.2)
    print(colors.BLUE + "Sua missão é coletar pistas, interrogar os suspeitos e resolver o caso.")
    sleep(0.2)
    print("Vamos começar!" + colors.END)
    print("\n---------------------------------------------------------------------------------\n")

    arvore = BinaryTree()

    root = arvore.add(colors.BLUE + "Você está no local do crime. O que você faz?" + colors.END,
                      colors.RED + "Você decide acusar alguém." + colors.END,
                      colors.GREEN + "Você decide procurar mais informações." + colors.END)

    root.left.left = Node("Você acusa a esposa, mas não há provas suficientes. Tente novamente.", final=True)
    root.left.right = Node("Você acusa o sócio, mas não há provas suficientes. Tente novamente.", final=True)

    root.right.left = arvore.add("Você encontra uma pista importante: uma pegada de sapato.",
                                 "Você decide acusar alguém com base na pegada.",
                                 "Você continua procurando mais informações.")

    root.right.right = arvore.add("Você encontra um álibi que descarta um dos suspeitos.",
                                  "Você decide acusar alguém baseado no álibi.",
                                  "Você continua procurando mais informações.")

    root.right.left.left = Node("Você acusa a esposa com base na pegada, mas não há provas suficientes. Tente novamente.", final=True)
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
