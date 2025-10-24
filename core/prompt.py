from colorama import Fore, Style

def get_user_input():
    return input(f"{Fore.CYAN}Nic>{Style.RESET_ALL} ")

def respond(message: str):
    print(f"{Fore.MAGENTA}Ignia>{Style.RESET_ALL} {message}")
