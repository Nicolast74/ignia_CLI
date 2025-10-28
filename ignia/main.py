import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from colorama import init
from core.memory import clear_memory, read_memory, save_message
from core.prompt import get_user_input, show_banner, clear_screen
from core.persona import generate_response
from core.display import display_message, show_typing
from core.utils import slow_print
from core.command_handler import handle_command

def main():
    ASSISTANT_NAME = "Ignia"
    init(autoreset=True)
    clear_screen()
    show_banner()
    slow_print(f"{ASSISTANT_NAME}> 🩷 Aku udah online nih, luv~ Ketik 'exit' buat aku istirahat ya.\n", 0.03)

    while True:
        user_msg = get_user_input()

        command_result = handle_command(user_msg)
        if command_result == "exit":
            show_typing()
            display_message("assistant", "Hehehe~ baik luv, sampai ketemu lagi 🩷", "magenta")
            break
        elif command_result == "continue":
            continue
        
        # Simpan pesan user
        save_message("user", user_msg)

        # Efek Ignia mikir dulu sebelum bales
        print(f"\n{ASSISTANT_NAME} ❤️: ", end="", flush=True)
        for dot in "...":
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(0.4)
        print(f"\r{ASSISTANT_NAME} ❤️: ", end="", flush=True)

        # Generate & tampilkan respons
        response = generate_response(user_msg)
        slow_print(response, 0.03)
        save_message("assistant", response)

    return 0

if __name__ == "__main__":
    sys.exit(main())
