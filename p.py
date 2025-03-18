import time
from colorama import Fore, Style, init

init(autoreset=True)

def print_design():
    design = [
        f"{Fore.RED}{Style.BRIGHT}*" * 40,
        f"{Fore.YELLOW}{Style.BRIGHT}*        WELCOME TO PYTHON ART        *",
        f"{Fore.GREEN}{Style.BRIGHT}*" * 40,
        f"{Fore.CYAN}{Style.BRIGHT}*        Enjoy coding with Python!       *",
        f"{Fore.BLUE}{Style.BRIGHT}*" * 40,
        f"{Fore.MAGENTA}{Style.BRIGHT}*        Have a great day!            *",
        f"{Fore.WHITE}{Style.BRIGHT}*" * 40,
    ]
    
    for line in design:
        print(line)
        time.sleep(0.3)  # Creates a smooth effect

if __name__ == "__main__":
    print_design()
