from cores import colors
from maquina import type_writer
import time
def mostrar_menu():
    time.sleep(0.2)
    print(colors.MAGENTA+"=" * 40+colors.END)
    print(" " * 12 + colors.DARKRED+"Bem-vindo ao Jogo!"+colors.END)
    time.sleep(0.2)
    print(colors.MAGENTA+"=" * 40+colors.END)
    opcao1 = colors.ORANGE+"1. Jogar\n"+colors.END
    opcao2 = colors.PURPLE+"2. Creditos\n"+colors.END
    opcao3 = colors.GREEN+"3. Configurações\n"+colors.END
    opcao4 = colors.RED+"4. Sair\n"+colors.END
    time.sleep(0.2)
    type_writer(opcao1)
    time.sleep(0.2)
    type_writer(opcao2)
    time.sleep(0.2)
    type_writer(opcao3)
    time.sleep(0.2)
    type_writer(opcao4)
    time.sleep(0.2)
    print(colors.MAGENTA+"=" * 40+colors.END)

def Jogar():
    print("\n" + "=" * 40)
    print("Iniciando um novo jogo...")
    print("=" * 40 + "\n")

def Creditos():
    print("\n" + "=" * 40)
  
    print("Carregando créditos...")
    print("=" * 40 + "\n")
    time.sleep(2)
    mensagem = colors.CYAN+"este jogo foi desenvolvido por :"+colors.END
    type_writer(mensagem)
    time.sleep(1)
    print(colors.random_color()+"\nmarco"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"joão"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"eville"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"julia"+colors.END)
    time.sleep(1)
    
   

def configuracoes():
    print("\n" + "=" * 40)
    print("Abrindo configurações...")
    print("=" * 40 + "\n")

def main():
    while True:
        mostrar_menu()
        time.sleep(0.2)
        escolha = input(colors.DARKBLUE+"Escolha uma opção (1-4): "+colors.END)

        if escolha == '1':
            Jogar()
            break
        elif escolha == '2':
            Creditos()
        elif escolha == '3':
            configuracoes()
        elif escolha == '4':
            print("\n" + "=" * 40)
            print("Saindo do jogo...")
            print("=" * 40)
            break
        else:
            print("\n" + "=" * 40)
            print("Opção inválida, por favor escolha novamente.")
            print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
