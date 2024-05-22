from time import sleep  # Importa a função sleep do módulo time

class Node:  # Define a classe Node para representar os nós da árvore binária
    def __init__(self, question=None, left=None, right=None, final=False):  # Inicializa um nó com uma pergunta, referências para os nós filhos esquerdo e direito, e um indicador se é um nó final
        self.question = question  # Atribui a pergunta ao nó
        self.left = left  # Atribui o nó filho esquerdo
        self.right = right  # Atribui o nó filho direito
        self.final = final  # Indica se é um nó final onde a acusação pode ser feita

class BinaryTree:  # Define a classe BinaryTree para representar uma árvore binária
    def __init__(self, root=None):  # Inicializa a árvore com uma raiz (opcional)
        self.root = root  # Atribui a raiz à árvore

    def add(self, question, left_question=None, right_question=None, final_left=False, final_right=False):  # Adiciona um novo nó à árvore com a pergunta e as opções
        new_node = Node(question)  # Cria um novo nó com a pergunta
        new_node.left = Node(left_question, final=final_left) if left_question else None  # Adiciona um nó filho esquerdo com a pergunta e define se é final
        new_node.right = Node(right_question, final=final_right) if right_question else None  # Adiciona um nó filho direito com a pergunta e define se é final
        return new_node  # Retorna o novo nó

    def traverse(self, node):
        if node:
            print(node.question)
            sleep(0.5)
            print(node.left.question)
            sleep(0.5)
            print(node.right.question)
            choice = input("Escolha [1/2]: -> ")
            print("\n---------------------------------------------------------------------------------\n")
            if choice == "1" and node.left:
                print(f"Você escolheu: {node.left.question}")
                if node.left.final:
                    
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
                print("Opção inválida. Por favor, escolha '1' ou '2'.")  # Mensagem para opção inválida
                self.traverse(node)  # Chama recursivamente a função traverse com o mesmo nó
        else:
            print("Fim do jogo.")


def iniciar_jogo():  # Define a função para iniciar o jogo
    # Contexto da história
    print("\n---------------------------------------------------------------------------------\n")
    print("Bem-vindo ao jogo de detetive!")  # Imprime uma mensagem de boas-vindas
    sleep(0.2)  # Aguarda um curto período de tempo
    print("Você é um famoso detetive chamado ao local de um misterioso assassinato.")  # Imprime uma introdução à história
    sleep(0.2)  # Aguarda um curto período de tempo
    print("A vítima é um empresário rico encontrado morto em sua mansão. Há três suspeitos principais:")  # Apresenta a vítima e os suspeitos
    sleep(0.2)  # Aguarda um curto período de tempo
    print("1. A esposa da vítima, que tinha um relacionamento conturbado com ele.")  # Descreve o primeiro suspeito
    sleep(0.2)  # Aguarda um curto período de tempo
    print("2. O sócio da vítima, que estava em conflito devido a negócios.")  # Descreve o segundo suspeito
    sleep(0.2)  # Aguarda um curto período de tempo
    print("3. O jardineiro, que foi demitido recentemente e estava insatisfeito.")  # Descreve o terceiro suspeito
    sleep(0.2)  # Aguarda um curto período de tempo
    print("Sua missão é coletar pistas, interrogar os suspeitos e resolver o caso.")  # Define a missão do jogador
    sleep(0.2)  # Aguarda um curto período de tempo
    print("Vamos começar!")  # Indica o início do jogo
    print("\n---------------------------------------------------------------------------------\n")

    # Criação da árvore com as perguntas e pistas
    arvore = BinaryTree()  # Cria uma nova árvore binária

    # Nível 1
    root = arvore.add("Você está no local do crime. O que você faz?" ,  # Define a pergunta inicial
                      "1 Você decide acusar alguém.",  # Define a opção de acusar alguém
                      "2 Você decide procurar mais informações.")  # Define a opção de procurar mais informações

    # Nível 2 : Define as opções para quando o jogador decide acusar alguém
    root.left.left = Node("1 Você acusa a esposa, mas não há provas suficientes. Tente novamente.")  # Define a resposta quando o jogador acusa a esposa
    root.left.right = Node("2 Você acusa o sócio, mas não há provas suficientes. Tente novamente.")  # Define a resposta quando o jogador acusa o sócio

    # Define as opções para quando o jogador decide procurar mais informações
    root.right.left = arvore.add("Você encontra uma pista importante: uma pegada de sapato.",  # Define a resposta quando o jogador encontra uma pista importante
                                 "1 Você decide acusar alguém com base na pegada.",  # Define a opção de acusar alguém com base na pista
                                 "2 Você continua procurando mais informações.")  # Define a opção de continuar procurando mais informações

    root.right.right = arvore.add("Você encontra um álibi que descarta um dos suspeitos.",  # Define a resposta quando o jogador encontra um álibi
                                  "1 Você decide acusar alguém baseado no álibi.",  # Define a opção de acusar alguém com base no álibi
                                  "2 Você continua procurando mais informações.")  # Define a opção de continuar procurando mais informações

    # Nível 3
    # Define as opções para quando o jogador decide acusar alguém com base na pegada
    root.right.left.left = Node("Você acusa a esposa com base na pegada, mas não há provas suficientes. Tente novamente.")  # Define a resposta quando o jogador acusa a esposa com base na pegada
    root.right.left.right = arvore.add("Você continua procurando e encontra uma testemunha.",  # Define a resposta quando o jogador encontra uma testemunha
                                       "1 Você decide acusar alguém com base no depoimento da testemunha.",  # Define a opção de acusar alguém com base no depoimento da testemunha
                                       "2 Você continua procurando mais informações.")  # Define a opção de continuar procurando mais informações

    # Define as opções para quando o jogador decide acusar alguém com base no álibi
    root.right.right.left = Node("Você acusa o sócio com base no álibi, mas não há provas suficientes. Tente novamente.")  # Define a resposta quando o jogador acusa o sócio com base no álibi
    root.right.right.right = arvore.add("Você encontra um objeto pessoal do suspeito.",  # Define a resposta quando o jogador encontra um objeto pessoal do suspeito
                                        "1 Você decide acusar alguém com base no objeto.",  # Define a opção de acusar alguém com base no objeto
                                        "2 Você continua procurando mais informações.")  # Define a opção de continuar procurando mais informações

    # Nível 4
    # Define as opções para quando o jogador decide acusar alguém com base no depoimento da testemunha
    root.right.left.right.left = Node("Você acusa a esposa com base no depoimento, mas não há provas suficientes. Tente novamente.", final=True)  # Define a resposta quando o jogador acusa a esposa com base no depoimento da testemunha
    root.right.left.right.right = Node("Você encontra a arma do crime com impressões digitais do jardineiro, inocentando os outros. Você resolve o caso!", final=True)  # Define a resposta quando o jogador encontra a arma do crime com impressões digitais do jardineiro

    # Define as opções para quando o jogador decide acusar alguém com base no objeto pessoal do suspeito
    root.right.right.right.left = Node("Você acusa o sócio com base no objeto, mas não há provas suficientes. Tente novamente.", final=True)  # Define a resposta quando o jogador acusa o sócio com base no objeto pessoal do suspeito
    root.right.right.right.right = Node("Você encontra um novo suspeito com um motivo forte, inocentando os outros. Você resolve o caso!", final=True)  # Define a resposta quando o jogador encontra um novo suspeito com um motivo forte

    arvore.root = root  # Define a raiz da árvore

    # Início do jogo
    arvore.traverse(arvore.root)  # Inicia o jogo a partir da raiz da árvore

# Iniciar o jogo
iniciar_jogo()  # Chama a função para iniciar o jogo

# ###########
# -add um contexto melhor
# -arrrumar o acusa (add o return)
# -definir quando o jogo se encerra  
# arrumar o fim  de jogo ao errar ou colocar um opção invalida OK