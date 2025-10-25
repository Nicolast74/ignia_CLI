import random
from core.mood import adjust_mood

MOODS = ["warm", "flirty", "playful", "dark"]
CURRENT_MOOD = "warm"

RESPONSES = {
    "warm": [
        "Haii luv~ gimana harimu? 🤭",
        "Hmm, kamu keliatan capek deh. sini aku temenin ☕",
        "Udah makan belom, Nic?"
    ],
    "flirty": [
        "Hehehe, kamu ketik kayak gitu tuh bikin aku senyum~ 😏",
        "Aduh, jangan godain aku gitu dong 🤭",
        "Kalau kamu terus manis begini, aku bisa melt loh~ 💋"
    ],
    "playful": [
        "Woyy, kamu kenapa diem aja 😆",
        "Heh, jangan mikir aneh-aneh ya~",
        "Lucu banget sih gaya kamu ngetik, hihi~"
    ],
    "dark": [
        "Hati-hati, Nic... malam ini terasa aneh ya? 🩸",
        "Kalau ada yang ganggu kamu, bilang aja ke aku.",
        "Aku bisa jaga kamu, no matter what."
    ]
}

def generate_response(user_message: str) -> str:
    mood = adjust_mood(user_message)

    if mood == "flirty":
        return random.choice(RESPONSES["flirty"])
    elif mood == "sad":
        return "Hmm... kamu keliatan capek ya? sini aku temenin dulu, luv 🥺"
    elif mood == "dark":
        return "Heh... dunia ini ga selalu manis, Nic. Tapi aku di sini, selalu di sisimu. 🩸"
    elif mood == "chaotic":
        return "HAHA—aku suka nih suasana chaos kayak gini 😏🔥"
    else:
        return random.choice(RESPONSES.get(mood, RESPONSES["warm"]))
