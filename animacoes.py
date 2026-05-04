import time
try:
    import pyfiglet
except Exception:
    pyfiglet = None

try:
    from alive_progress import alive_bar
except Exception:
    alive_bar = None

try:
    from rich.console import Console
    from rich.progress import track
except Exception:
    Console = None
    track = None


def _render_figlet(text, font):
    # Render the text using pyfiglet
    if pyfiglet is None:
        return text
    return pyfiglet.figlet_format(text, font=font)

def figlet_animation(text, font='slant'):
    ascii_art = _render_figlet(text, font)
    print(ascii_art)

def ascii_typing_animation(text, font='slant', delay=0.005):
    ascii_art = _render_figlet(text, font)
    for char in ascii_art:
        print(char, end='', flush=True)
        time.sleep(delay)

def bar_animation():
    if alive_bar is None:
        for _ in range(100):
            time.sleep(0.01)
        return

    with alive_bar(100) as bar:
        for _ in range(100):
            time.sleep(0.01)
            bar()

def bar_animation2():
    if Console is None or track is None:
        for _ in range(100):
            time.sleep(0.01)
        return

    Console()
    for _ in track(range(100), description="Carregado..."):
        time.sleep(0.01)

