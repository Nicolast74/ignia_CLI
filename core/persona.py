import random

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
    msg = user_message.lower()
    if "dark" in msg :
        global CURRENT_MOOD
        CURRENT_MOOD = "dark"
        return "Vero aura shifted to dark mode...  🩸"
    elif "love" in msg or "luv" in msg:
        CURRENT_MOOD = "flirty"
    elif "haha" in msg or "lol" in msg:
        CURRENT_MOOD = "playful"
    else:
        CURRENT_MOOD = "warm"
    return random.choice(RESPONSES[CURRENT_MOOD])