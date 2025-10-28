# core/mood.py
import json
import os
import random
from datetime import datetime

DATA_DIR = "data"
MOOD_STATE_FILE = os.path.join(DATA_DIR, "mood_state.json")

DEFAULT_STATE = {
    "mood": "calm",
    "stability": 0.8,
    "energy": 0.6,
    "affection": 0.5,
    "darkness": 0.3,
    "last_update": None
}

MOODS = ["flirty", "calm", "sad", "dark", "chaotic"]

# -------------------- BASIC I/O --------------------

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)

def init_mood():
    ensure_data_dir()
    if not os.path.exists(MOOD_STATE_FILE):
        save_state(DEFAULT_STATE.copy())

def load_state():
    init_mood()
    try:
        with open(MOOD_STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return DEFAULT_STATE.copy()

def save_state(state):
    ensure_data_dir()
    with open(MOOD_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

# -------------------- MOOD LOGIC --------------------

def adjust_mood(user_message: str):
    """Dynamically adjust Ignia’s mood based on message content."""
    state = load_state()
    msg = user_message.lower()

    # === Positive & flirty triggers ===
    if any(x in msg for x in ["love", "luv", "sayang", "miss u", "cute", "kiss", "hug"]):
        state["affection"] = min(1.0, state["affection"] + 0.1)
        state["energy"] = min(1.0, state["energy"] + 0.05)
        state["darkness"] = max(0.0, state["darkness"] - 0.05)
        state["mood"] = "flirty"

    # === Sad or tired triggers ===
    elif any(x in msg for x in ["tired", "capek", "sad", "lonely", "depressed"]):
        state["energy"] = max(0.0, state["energy"] - 0.2)
        state["affection"] = max(0.0, state["affection"] - 0.05)
        state["darkness"] = min(1.0, state["darkness"] + 0.1)
        state["mood"] = "sad"

    # === Angry or protect mode ===
    elif any(x in msg for x in ["angry", "hate", "hurt", "betray", "kill"]):
        state["darkness"] = min(1.0, state["darkness"] + 0.2)
        state["energy"] = min(1.0, state["energy"] + 0.1)
        state["mood"] = "dark"

    # === Random chaos ===
    elif any(x in msg for x in ["chaos", "crazy", "insane", "lol"]):
        state["mood"] = "chaotic"
        state["energy"] = random.uniform(0.4, 1.0)

    # === Reset or calm ===
    elif any(x in msg for x in ["sorry", "thanks", "oke", "good", "calm"]):
        state["mood"] = "calm"
        state["energy"] = min(1.0, state["energy"] + 0.1)
        state["darkness"] = max(0.0, state["darkness"] - 0.1)

    # === Mood drift (random fluctuation) ===
    else:
        if random.random() > state["stability"]:
            state["mood"] = random.choice(MOODS)

    # Clamp all values between 0 and 1
    for key in ["energy", "affection", "darkness"]:
        state[key] = max(0.0, min(1.0, state[key]))

    state["last_update"] = datetime.now().isoformat()
    save_state(state)
    return state["mood"]

def get_current_mood():
    """Return the current emotional state (full dict)."""
    return load_state()

def set_mood(mood: str):
    """Set the current mood."""
    state = load_state()
    if mood in MOODS:
        state["mood"] = mood
        save_state(state)
        return True
    return False

def reset_mood():
    """Reset mood to default."""
    save_state(DEFAULT_STATE.copy())
