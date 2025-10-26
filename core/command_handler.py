from core.display import display_message
from core.memory import clear_memory, read_memory

def handle_command(user_msg):
    if user_msg.lower() == "exit":
        return "exit"

    elif user_msg.lower() == "forget":
        from core.display import show_typing
        show_typing()
        clear_memory()
        display_message("assistant", "...done. Aku udah lupa semuanya sekarang 🩸", "red")
        return "continue"

    elif user_msg.lower() == "history":
        memory = read_memory()
        if not memory:
            display_message("assistant", "Aku belum ingat apa-apa, luv~ 🤭", "yellow")
        else:
            display_message("assistant", "Aku masih ingat percakapan kita 💭", "cyan")
            for item in memory:
                display_message(item["role"], item["content"], "white")
        return "continue"

    elif user_msg.startswith("/mood"):
        from core.mood import load_state
        state = load_state()
        mood = state.get("mood", "unknown")
        stability = state.get("stability", 0)
        display_message("assistant", f"🩷 Mood: {mood}, Stability: {stability:.2f}", "cyan")
        return "continue"

    elif user_msg.startswith("/setmood"):
        from core.mood import set_mood, MOODS
        parts = user_msg.split(maxsplit=1)
        if len(parts) < 2:
            display_message("assistant", "Ketik `/setmood <mood>` ya luv~", "yellow")
            return "continue"

        new_mood = parts[1].strip().lower()
        if set_mood(new_mood):
            display_message("assistant", f"💫 Oke, sekarang aku lagi {new_mood} nih~", "magenta")
        else:
            display_message("assistant", f"Mood '{new_mood}' ga dikenal 🌀\nPilih dari: {', '.join(MOODS)}", "red")
        return "continue"

    return None
