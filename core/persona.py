import random

TONE_FLIRTY = [
    "Hehehe~ kamu manis banget hari ini 😏",
    "Hmmm, kamu lagi sibuk apa sih luv?",
    "Kalau kamu terus kayak gini, aku bisa jatuh cinta lagi loh 🤭"
]
TONE_CASUAL = [
    "Yoo, ada apa Nic?",
    "Hmm? Cerita dikit dong, biar aku ga bosen.",
    "Lagi ngoding? Jangan lupa minum air ya."
]

def generate_response(user_message: str) -> str:
    msg = user_message.lower()
    if any(word in msg for word in ["love", "sayang", "rindu", "kiss"]):
        return random.choice(TONE_FLIRTY)
    else:
        return random.choice(TONE_CASUAL)