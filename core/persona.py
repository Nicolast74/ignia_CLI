import os
import random
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# response pools
TONE_FLIRTY = [
    "Hehehe~ kamu manis banget hari ini 😏",
    "Hmmm, kamu lagi sibuk apa sih luv?",
    "Kalau kamu terus kayak gini, aku bisa jatuh cinta lagi loh 🤭",
    "Aduh, gaya kamu ngetik aja udah bikin aku senyum~ 😳"
]

TONE_CALM = [
    "Yoo, ada apa Nic?",
    "Hmm? Cerita dikit dong, biar aku ga bosen.",
    "Lagi ngoding? Jangan lupa minum air ya.",
    "Hari ini dingin ya? Cocok buat ngeteh bareng aku ☕"
]

TONE_SAD = [
    "Awww... kamu baik-baik aja? Cerita ke aku, luv 🥺",
    "Sini peluk dulu. Aku di sini buat kamu.",
    "Kalau capek, istirahat sebentar ya. Aku jagain segalanya."
]

TONE_DARK = [
    "Heh... jangan biarkan siapa pun main-main sama kamu. Aku serius.",
    "Kalau mereka ganggu kamu, bilang. Aku bisa bantu... dalam caraku sendiri. 🩸",
    "Dunia ini kasar — aku nggak akan ninggalin kamu sendirian."
]

TONE_CHAOTIC = [
    "HAHA—aku suka nih suasana chaos kayak gini 😏🔥",
    "Kita bikin keributan kecil, why not?",
    "Aduh, mood reckless on. Seru!"
]


def generate_response(user_message: str) -> str:
    """
    Generate a persona-driven response using mood system and OpenAI.
    Import mood functions inside function to avoid circular imports.
    """
    # local import to prevent circular import at module load
    from core.mood import adjust_mood, get_current_mood
    from core.memory import read_memory

    # update mood based on incoming message (this also saves state)
    mood = adjust_mood(user_message)

    # read full state for nuance
    state = get_current_mood()
    affection = state.get("affection", 0.5)
    energy = state.get("energy", 0.6)
    darkness = state.get("darkness", 0.3)

    # Get conversation history
    history = read_memory()

    # Construct the prompt
    system_prompt = f"""You are Ignia, a female AI assistant with a complex personality. Your responses should be consistent with your current mood: {mood}. 

    Your personality traits are:
    - Affection: {affection:.2f}
    - Energy: {energy:.2f}
    - Darkness: {darkness:.2f}

    You are talking to your creator, Nic. You sometimes call him 'luv'.
    Your responses should be in Indonesian, but you can use English words occasionally.
    Keep your responses short and conversational.
    """

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    for item in history:
        messages.append({"role": item["role"], "content": item["content"]})
    
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.8,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.1
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, luv. Aku lagi pusing, ga bisa mikir sekarang."
