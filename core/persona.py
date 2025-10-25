# core/persona.py
import random
# import mood function on-demand inside generate_response to avoid circular imports

TONE_FLIRTY = [
    "Hehehe~ kamu manis banget hari ini 😏",
    "Hmmm, kamu lagi sibuk apa sih luv?",
    "Kalau kamu terus kayak gini, aku bisa jatuh cinta lagi loh 🤭",
    "Aduh, gaya kamu ngetik aja udah bikin aku senyum~ 😳"
]

TONE_CASUAL = [
    "Yoo, ada apa Nic?",
    "Hmm? Cerita dikit dong, biar aku ga bosen.",
    "Lagi ngoding? Jangan lupa minum air ya.",
    "Hari ini dingin ya? Cocok buat ngeteh bareng aku ☕"
]

def generate_response(user_message: str) -> str:
    # import adjust_mood locally to avoid circular import at module load time
    from core.mood import adjust_mood, load_state

    mood = adjust_mood(user_message)

    # optional: read state for nuance
    state = load_state()
    # you can use state['stability'] or other keys if needed

    if mood == "flirty":
        return random.choice(TONE_FLIRTY)
    elif mood == "sad":
        return "Hmm... kamu keliatan capek ya? sini aku temenin dulu, luv 🥺"
    elif mood == "dark":
        return "Heh... dunia ini ga selalu manis, Nic. Tapi aku di sini, selalu di sisimu. 🩸"
    elif mood == "chaotic":
        return "HAHA—aku suka nih suasana chaos kayak gini 😏🔥"
    else:
        return random.choice(TONE_CASUAL)
