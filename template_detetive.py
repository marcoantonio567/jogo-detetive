class Nodo:
    def __init__(self, pergunta=None, resposta_sim=None, resposta_nao=None, suspeito=None, descricao=None):
        self.pergunta = pergunta
        self.resposta_sim = resposta_sim
        self.resposta_nao = resposta_nao
        self.suspeito = suspeito
        self.descricao = descricao

class JogoDetetive:
    def __init__(self):
        # Descrições dos suspeitos
        self.descricoes = {
            "João": "João é um homem de 30 anos, trabalha como jardineiro e estava na cena do crime.",
            "Maria": "Maria é uma mulher de 25 anos, vizinha da vítima e ouviu gritos na noite do crime.",
            "Carlos": "Carlos é um homem de 40 anos, trabalha como eletricista e tem um histórico criminal.",
            "Ana": "Ana é uma mulher de 35 anos, ex-namorada da vítima e foi vista perto da cena do crime."
        }
        
        # Construir a árvore binária de perguntas
        self.raiz = Nodo(
            pergunta="A vítima estava no jardim?",
            resposta_sim=Nodo(
                pergunta="Havia pegadas na terra?",
                resposta_sim=Nodo(suspeito="João"),
                resposta_nao=Nodo(suspeito="Carlos")
            ),
            resposta_nao=Nodo(
                pergunta="Havia sinais de arrombamento?",
                resposta_sim=Nodo(suspeito="Carlos"),
                resposta_nao=Nodo(
                    pergunta="Alguém ouviu gritos?",
                    resposta_sim=Nodo(suspeito="Maria"),
                    resposta_nao=Nodo(suspeito="Ana")
                )
            )
        )

    def dar_contexto(self):
        print("Você é um detetive encarregado de resolver um misterioso assassinato.")
        print("A vítima foi encontrada em sua casa e há quatro suspeitos: João, Maria, Carlos e Ana.")
        print("Interrogue as pessoas e visite os locais para juntar pistas e encontrar o assassino.\n")
    
    def ver_descricoes(self):
        print("Descrições dos suspeitos:")
        for suspeito, descricao in self.descricoes.items():
            print(f"{suspeito}: {descricao}")
        print()
    
    def interrogar(self, nodo):
        if nodo.suspeito:
            return nodo.suspeito
        resposta = input(nodo.pergunta + " (sim/nao): ").strip().lower()
        if resposta == "sim":
            return self.interrogar(nodo.resposta_sim)
        else:
            return self.interrogar(nodo.resposta_nao)
    
    def jogar(self):
        self.dar_contexto()
        while True:
            print("O que você quer fazer?")
            print("1. Interrogar pessoas e visitar locais")
            print("2. Ver descrições dos suspeitos")
            print("3. Acusar alguém")
            print("4. Sair do jogo")
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                suspeito = self.interrogar(self.raiz)
                print(f"Após a investigação, você suspeita que o assassino é {suspeito}.")
            elif opcao == "2":
                self.ver_descricoes()
            elif opcao == "3":
                suspeito = input("Quem você quer acusar? ").strip()
                if suspeito in self.descricoes:
                    print(f"Você acusou {suspeito}.")
                    print("Investigação finalizada.\n")
                    break
                else:
                    print("Suspeito inválido. Tente novamente.")
            elif opcao == "4":
                print("Saindo do jogo. Até a próxima!")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    jogo = JogoDetetive()
    jogo.jogar()
