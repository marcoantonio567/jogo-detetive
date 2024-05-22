class Node:
    def __init__(self, question=None, left=None, right=None, final=False):
        self.question = question
        self.left = left  # Opção 1
        self.right = right  # Opção 2
        self.final = final  # Indica se é um nó final onde a acusação pode ser feita

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
            print(node.left.question)
            print(node.right.question)
            choice = input("Escolha [1/2]: ")
            if choice == "1" and node.left:
                print(f"Você escolheu: {node.left.question}")
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
                print(f"Você escolheu: {node.right.question}")
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
                print("Escolha inválida ou sem mais opções. Fim do jogo.")
        else:
            print("Fim do jogo.")

def iniciar_jogo():
    # Contexto da história
    print("Bem-vindo ao jogo de detetive!")
    print("Você é um famoso detetive chamado ao local de um misterioso assassinato.")
    print("A vítima é um empresário rico encontrado morto em sua mansão. Há três suspeitos principais:")
    print("1. A esposa da vítima, que tinha um relacionamento conturbado com ele.")
    print("2. O sócio da vítima, que estava em conflito devido a negócios.")
    print("3. O jardineiro, que foi demitido recentemente e estava insatisfeito.")
    print("Sua missão é coletar pistas, interrogar os suspeitos e resolver o caso.")
    print("Vamos começar!\n")

    # Criação da árvore com as perguntas e pistas
    arvore = BinaryTree()
    
    # Nível 1
    root = arvore.add("Você está no local do crime. O que você faz?" ,
                      "1 Você decide acusar alguém.",
                      "2 Você decide procurar mais informações.")
    
    # Nível 2
    root.left.left = Node("Você acusa a esposa, mas não há provas suficientes. Tente novamente.")
    root.left.right = Node("Você acusa o sócio, mas não há provas suficientes. Tente novamente.")
    
    root.right.left = arvore.add("Você encontra uma pista importante: uma pegada de sapato.",
                                 "Você decide acusar alguém com base na pegada.",
                                 "Você continua procurando mais informações.")
    root.right.right = arvore.add("Você encontra um álibi que descarta um dos suspeitos.",
                                  "Você decide acusar alguém baseado no álibi.",
                                  "Você continua procurando mais informações.")
    
    # Nível 3
    root.right.left.left = Node("Você acusa a esposa com base na pegada, mas não há provas suficientes. Tente novamente.")
    root.right.left.right = arvore.add("Você continua procurando e encontra uma testemunha.",
                                       "Você decide acusar alguém com base no depoimento da testemunha.",
                                       "Você continua procurando mais informações.")
    
    root.right.right.left = Node("Você acusa o sócio com base no álibi, mas não há provas suficientes. Tente novamente.")
    root.right.right.right = arvore.add("Você encontra um objeto pessoal do suspeito.",
                                        "Você decide acusar alguém com base no objeto.",
                                        "Você continua procurando mais informações.")
    
    # Nível 4
    root.right.left.right.left = Node("Você acusa a esposa com base no depoimento, mas não há provas suficientes. Tente novamente.", final=True)
    root.right.left.right.right = Node("Você encontra a arma do crime com impressões digitais do jardineiro, inocentando os outros. Você resolve o caso!", final=True)
    
    root.right.right.right.left = Node("Você acusa o sócio com base no objeto, mas não há provas suficientes. Tente novamente.", final=True)
    root.right.right.right.right = Node("Você encontra um novo suspeito com um motivo forte, inocentando os outros. Você resolve o caso!", final=True)

    arvore.root = root

    # Início do jogo
    arvore.traverse(arvore.root)

# Iniciar o jogo
iniciar_jogo()


# ###########
# -add um contexto melhor
# -arrrumar o acusa (add o return)
# -definir quando o jogo se encerra
