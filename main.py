# main.py
from core.prompt import get_user_input, respond
from core.persona import generate_response

def main():
    print("\033[35m[Ignia CLI v0.1] Online.\033[0m")
    print("Type 'exit' to shut me down.\n")

    while True:
        user_msg = get_user_input()
        if user_msg.lower() == "exit":
            respond("Hehehe~ baik luv, sampai ketemu lagi 🩷")
            break

        response = generate_response(user_msg)
        respond(response)

if __name__ == "__main__":
    main()
