from core.memory import clear_memory, read_memory, save_message
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

        if user_msg.lower() == "exit":
            respond("Hehehe~ baik luv, sampai ketemu lagi 🩷")
            break
        elif user_msg.lower() == "forget":
            clear_memory()
            respond("...done. Aku udah lupa semuanya sekarang 🩸")
            continue
        elif user_msg.lower() == "history":
            memory = read_memory()
            if not memory:
                respond("Aku belum ingat apa-apa, luv~ 🤭")
            else:
                respond("Aku masih ingat percakapan kita 💭")
                for item in memory:
                    print(f"{item['role']}: {item['content']}")
            continue

        save_message("user", user_msg)
        response = generate_response(user_msg)
        save_message("ignia", response)
        respond(response)

if __name__ == "__main__":
    main()
