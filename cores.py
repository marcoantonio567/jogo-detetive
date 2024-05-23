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

# Usa as cores definidas
print(colors.RED + 'Este texto será vermelho!' + colors.END)
print(colors.BOLD + 'Este texto será em negrito!' + colors.END)
print(colors.UNDERLINE + 'Este texto será sublinhado!' + colors.END)
print(colors.GREEN + 'Este texto será verde!' + colors.END)
