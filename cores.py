# Define os códigos de escape ANSI para cores
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    # Cores adicionais
    BLACK = '\033[30m'
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

# Usa as cores definidas
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