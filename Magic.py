# job.py

import time
import itertools
from colorama import Fore, Style, init

class Job:
    def __init__(self, prefix="(∩^o^)⊃━☆", base_string=". ݁₊ ⊹ . ݁˖ . ݁˗ˏˋDONEˎˊ˗", colors=None):
        # Initialisieren von colorama
        init()

        # Standardfarben definieren, falls keine angegeben sind
        if colors is None:
            colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

        self.prefix = prefix
        self.base_string = base_string
        self.colors = colors

    def colored_string(self, colors, string):
        colored_chars = [colors[i % len(colors)] + char for i, char in enumerate(string)]
        return ''.join(colored_chars) + Style.RESET_ALL

    def done(self, delay=0.1):
        try:
            print("\n\n")
            for i in itertools.cycle(range(len(self.colors))):
                current_colors = self.colors[i:] + self.colors[:i]  # Farbrotation
                print(f"{self.prefix} {self.colored_string(current_colors, self.base_string)}", end='\r', flush=True)
                time.sleep(delay)
        except KeyboardInterrupt:
            # Beenden der Schleife bei Tastendruck
            print(Style.RESET_ALL)  # Terminalfarben zurücksetzen
            print("\n\nMagic Over\n\n")
