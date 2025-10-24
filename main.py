from core.prompt import get_user_input, respond, show_banner, clear_screen
from core.persona import generate_response
from core.utils import clean_input, slow_print
from colorama import init

def main():
    init(autoreset=True)
    clear_screen()
    show_banner()
    slow_print("Ignia> 🩷 Aku udah online nih, luv~ Ketik 'exit' buat aku istirahat ya.\n", 0.03)

    while True:
        user_msg = get_user_input()
        user_msg = clean_input(user_msg)

        if user_msg.lower() == "exit":
            respond("Hehehe~ baik luv, sampai ketemu lagi 🩷")
            break

        response = generate_response(user_msg)
        slow_print(f"Ignia> {response}", 0.02)

if __name__ == "__main__":
    main()
