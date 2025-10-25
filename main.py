from core.memory import clear_memory, read_memory, save_message
from core.prompt import get_user_input, show_banner, clear_screen
from core.persona import generate_response
from core.utils import slow_print
from colorama import init
from core.display import display_message, show_typing

def main():
    init(autoreset=True)
    clear_screen()
    show_banner()
    slow_print("Ignia> 🩷 Aku udah online nih, luv~ Ketik 'exit' buat aku istirahat ya.\n", 0.03)

    while True:
        user_msg = get_user_input()

        if user_msg.lower() == "exit":
            show_typing()
            display_message("assistant", "Hehehe~ baik luv, sampai ketemu lagi 🩷", "magenta")
            break
        elif user_msg.lower() == "forget":
            clear_memory()
            show_typing()
            display_message("assistant", "...done. Aku udah lupa semuanya sekarang 🩸", "red")
            continue
        elif user_msg.lower() == "history":
            memory = read_memory()
            if not memory:
                display_message("assistant", "Aku belum ingat apa-apa, luv~ 🤭", "yellow")
            else:
                display_message("assistant", "Aku masih ingat percakapan kita 💭", "cyan")
                for item in memory:
                    display_message(item["role"], item["content"], "white")
            continue

        # Save user input
        save_message("user", user_msg)
        #display_message("user", user_msg, "cyan")

        # Generate and show response
        show_typing()
        response = generate_response(user_msg)
        save_message("ignia", response)
        display_message("assistant", response, "magenta")

if __name__ == "__main__":
    main()
