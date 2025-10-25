#prompt.py
from colorama import Fore, Style
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(f"{Fore.MAGENTA}╔══════════════════════════════╗")
    print(f"{Fore.MAGENTA}║{Fore.CYAN}      Ignia CLI v0.1          {Fore.MAGENTA}║")
    print(f"{Fore.MAGENTA}╚══════════════════════════════╝{Style.RESET_ALL}\n")

def get_user_input():
    return input(f"{Fore.CYAN}You> {Style.RESET_ALL}")

def respond(message: str):
    print(f"{Fore.MAGENTA}Ignia> {Style.RESET_ALL}{message}")
