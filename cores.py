import random
import time
import sys

# Define os códigos de escape ANSI para cores
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
   
    END = '\033[0m'
    
    WHITE = '\033[37m'
    MAGENTA = '\033[35m'
    ORANGE = '\033[33m'
    GRAY = '\033[90m'
    LIGHTGRAY = '\033[37m'
    LIGHTBLUE = '\033[94m'
    LIGHTGREEN = '\033[92m'
    LIGHTCYAN = '\033[96m'
    LIGHTRED = '\033[91m'
    LIGHTPURPLE = '\033[95m'
    DARKRED = '\033[31m'
    DARKGREEN = '\033[32m'
    DARKYELLOW = '\033[33m'
    DARKBLUE = '\033[34m'
    DARKMAGENTA = '\033[35m'
    DARKWHITE = '\033[37m'
    LIGHTYELLOW = '\033[93m'
    LIGHTMAGENTA = '\033[95m'

    @staticmethod
    def random_color():
        color_attributes = [attr for attr in dir(colors) if not callable(getattr(colors, attr)) and not attr.startswith("__")]
        color_name = random.choice(color_attributes)
        return getattr(colors, color_name)


"""print(colors.RED + 'Este texto será vermelho!' + colors.END)
print(colors.BOLD + 'Este texto será em negrito!' + colors.END)
print(colors.UNDERLINE + 'Este texto será sublinhado!' + colors.END)
print(colors.GREEN + 'Este texto será verde!' + colors.END)
print(colors.LIGHTBLUE + 'Este texto será azul claro!' + colors.END)
print(colors.LIGHTGREEN + 'Este texto será verde claro!' + colors.END)
print(colors.LIGHTRED + 'Este texto será vermelho claro!' + colors.END)
print(colors.LIGHTPURPLE + 'Este texto será roxo claro!' + colors.END)
print(colors.LIGHTCYAN + 'Este texto será ciano claro!' + colors.END)
"""