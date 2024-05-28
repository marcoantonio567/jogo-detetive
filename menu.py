from cores import colors
from maquina import type_writer
import time
from animacoes import ascii_typing_animation , figlet_animation , barra , barra2
from historia_marco import iniciar_jogo
from historia_julia import iniciar
from historia_eville import jogo
from historia_jao import jogar2
def mostrar_menu():
    time.sleep(0.2)
    wellcome = "Bem vindo ao Jogo !"
    ascii_typing_animation(wellcome)

    time.sleep(0.2)
    opcao1 = colors.ORANGE+"1. Jogar\n"+colors.END
    opcao2 = colors.PURPLE+"2. Créditos\n"+colors.END
    opcao3 = colors.GREEN+"3. Fases\n"+colors.END
    opcao4 = colors.RED+"4. Sair\n"+colors.END
    #time.sleep(0.2)
    type_writer(opcao1)
    #time.sleep(0.2)
    type_writer(opcao2)
    #time.sleep(0.2)
    type_writer(opcao3)
    #time.sleep(0.2)
    type_writer(opcao4)
    #time.sleep(0.2)
    print(colors.MAGENTA+"=" * 40+colors.END)

def Jogar():
    figlet_animation("Iniciando Jogo")
    print("\n" + "=" * 40)
    barra()
    iniciar()
def Creditos():
    figlet_animation("CREDITOS")
    print("\n" + "=" * 40)
    print("Carregando créditos...")
    barra()
    
    print("=" * 40 + "\n")
    time.sleep(2)
    mensagem = colors.CYAN+"Este jogo foi desenvolvido por :"+colors.END
    type_writer(mensagem)
    time.sleep(1)
    print(colors.random_color()+"\nMarco"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"João"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"Eville"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"Julia"+colors.END)
    time.sleep(1)

def Fases():
    figlet_animation("Fases")
    print("\n" + "=" * 40)
    print("Abrindo Fases...")
    print("=" * 40 )
    barra2()
    def historias():
        while True:
            msg = colors.CYAN + "Escolha a história que você deseja iniciar: " + colors.END
            type_writer(msg)
            time.sleep(1)
            print(colors.random_color() + "\n1. Julia" + colors.END)
            time.sleep(0.2)
            print(colors.random_color() + "2. Eville" + colors.END)
            time.sleep(0.2)
            print(colors.random_color() + "3. Marco" + colors.END)
            time.sleep(0.2)
            print(colors.random_color() + "4. João" + colors.END)
            time.sleep(0.2)
            print(colors.random_color() + "5. Voltar" + colors.END)
            time.sleep(1)
            print(colors.DARKBLUE + "Escolha uma opção (1-5): " + colors.END)

            escolha = input()

            if escolha.isdigit():
                escolha = int(escolha)
                if 1 <= escolha <= 5:
                    if escolha ==1:
                        print(colors.CYAN + f"Você escolheu a opção {escolha}!" + colors.END)
                        barra()
                        iniciar()
                    if escolha ==2:
                        print(colors.CYAN + f"Você escolheu a opção {escolha}!" + colors.END)
                        barra()
                        jogo()
                    if escolha ==3:
                        print(colors.CYAN + f"Você escolheu a opção {escolha}!" + colors.END)
                        barra()
                        iniciar_jogo()
                    if escolha ==4:
                        print(colors.CYAN + f"Você escolheu a opção {escolha}!" + colors.END)
                        barra()
                        jogar2()
                    if escolha == 5:
                        print(colors.CYAN + f"Você escolheu a opção {escolha}!" + colors.END)
                        barra()
                        main()
                    # else:
                    #     print(colors.CYAN + f"Você escolheu a opção {escolha}!" + colors.END)
                else:
                    print(colors.CYAN + "Escolha inválida! Por favor, escolha um número entre 1 e 5." + colors.END)
            else:
                print(colors.CYAN + "Entrada inválida! Por favor, digite um número." + colors.END)

            time.sleep(1)
        
        
    historias()
        

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
            Fases()
            break
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
