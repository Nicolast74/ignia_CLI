from core.prompt import get_user_input, respond
from core.persona import generate_response
from core.utils import clean_input
from colorama import init

def main():
    init(autoreset=True)
    respond("🩷 [Ignia CLI v0.1] Online. Ketik 'exit' untuk keluar.\n")

    while True:
        user_msg = get_user_input()
        user_msg = clean_input(user_msg)

        if user_msg.lower() == "exit":
            respond("Hehehe~ baik luv, sampai ketemu lagi 🩷")
            break

        response = generate_response(user_msg)
        respond(response)

if __name__ == "__main__":
    main()
