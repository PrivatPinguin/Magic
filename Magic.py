# job.py

import time
import itertools
from colorama import Fore, Style, init

class Job:
    def __init__(self, prefix="(∩^o^)⊃━☆", base_string=". ݁₊ ⊹ . ݁˖ . ݁˗ˏˋDONEˎˊ˗", colors=None):
        # Init
        init()

        # set STD colors
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
                current_colors = self.colors[i:] + self.colors[:i]
                print(f"{self.prefix} {self.colored_string(current_colors, self.base_string)}", end='\r', flush=True)
                time.sleep(delay)
        except KeyboardInterrupt:
            # quit on key
            print(Style.RESET_ALL)  # reset colors
            print("\n\nMagic Over\n\n")
