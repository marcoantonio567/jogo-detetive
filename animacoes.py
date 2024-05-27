import pyfiglet
import time
from asciimatics import *
import pyfiglet
from alive_progress import alive_bar
from rich.console import Console
from rich.progress import track

def ascii_typing_animation(text, font='slant', delay=0.005):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    for char in ascii_art:
        print(char, end='', flush=True)
        time.sleep(delay)

#ascii_typing_animation("Hello World")

# Função para animação com pyfiglet
def figlet_animation(text, font='slant'):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(ascii_art)


def barra():
    with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()


def barra2():
    console = Console()
    for task in track(range(100), description="Carregado..."):
        time.sleep(0.01)

