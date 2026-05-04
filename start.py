from cores import colors
from maquina import type_writer
import time
from animations import ascii_typing_animation , figlet_animation , bar_animation , bar_animation2
from historia_marco import start_part3
from historia_julia import start_part1
from historia_eville import start_part2
from historia_jao import start_part4

def show_menu():
    time.sleep(0.2)
    welcome = "Bem vindo ao Jogo !"
    ascii_typing_animation(welcome)

    time.sleep(0.2)
    option1 = colors.ORANGE+"\n1. Jogar\n"+colors.END
    option2 = colors.PURPLE+"2. Créditos\n"+colors.END
    option3 = colors.GREEN+"3. Fases\n"+colors.END
    option4 = colors.RED+"4. Sair\n"+colors.END
    
    type_writer(option1)
    type_writer(option2)
    type_writer(option3)
    type_writer(option4)
    
    print(colors.MAGENTA+"=" * 40+colors.END)

def play():
    figlet_animation("Iniciando Jogo")
    print("\n" + "=" * 40)
    bar_animation()
    start_part1()


def Credits():
    figlet_animation("CREDITOS")
    print("\n" + "=" * 40)
    print("Carregando créditos...")
    bar_animation()
    print("=" * 40 + "\n")
    time.sleep(2)
    mesage = colors.CYAN+"Este jogo foi desenvolvido por :"+colors.END
    type_writer(mesage)
    time.sleep(1)
    print(colors.random_color()+"\nMarco"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"João"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"Eville"+colors.END)
    time.sleep(0.2)
    print(colors.random_color()+"Julia"+colors.END)
    time.sleep(1)

def phases():
    figlet_animation("Fases")
    print("\n" + "=" * 40)
    print("Abrindo Fases...")
    print("=" * 40 )
    bar_animation2()
    def stories():
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

            choices = input()

            if choices.isdigit():
                choices = int(choices)
                if 1 <= choices <= 5:
                    if choices ==1:
                        print(colors.CYAN + f"Você escolheu a opção {choices}!" + colors.END)
                        bar_animation()
                        start_part1()
                    if choices ==2:
                        print(colors.CYAN + f"Você escolheu a opção {choices}!" + colors.END)
                        bar_animation()
                        start_part2()
                    if choices ==3:
                        print(colors.CYAN + f"Você escolheu a opção {choices}!" + colors.END)
                        bar_animation()
                        start_part3()
                    if choices ==4:
                        print(colors.CYAN + f"Você escolheu a opção {choices}!" + colors.END)
                        bar_animation()
                        start_part4()
                    if choices == 5:
                        print(colors.CYAN + f"Você escolheu a opção {choices}!" + colors.END)
                        bar_animation()
                        main()
                else:
                    print(colors.CYAN + "Escolha inválida! Por favor, escolha um número entre 1 e 5." + colors.END)
            else:
                print(colors.CYAN + "Entrada inválida! Por favor, digite um número." + colors.END)

            time.sleep(1)
        
        
    stories()
        

def main():
    while True:
        show_menu()
        time.sleep(0.2)
        choices = input(colors.DARKBLUE+"Escolha uma opção (1-4): "+colors.END)

        if choices == '1':
            play()
            break
        elif choices == '2':
            Credits()
        elif choices == '3':
            phases()
            break
        elif choices == '4':
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
