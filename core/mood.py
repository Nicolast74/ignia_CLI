# core/mood.py
import json
import os
import random

DATA_DIR = "data"
STATE_FILE = os.path.join(DATA_DIR, "persona_state.json")

DEFAULT_STATE = {
    "mood": "calm",
    "stability": 0.75  # 0..1, higher = mood lebih susah berubah
}

MOODS = ["calm", "flirty", "sad", "dark", "chaotic"]

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)

def init_state():
    """Ensure persona state file exists and has default keys."""
    ensure_data_dir()
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE.copy())

def load_state():
    """Load state, safely merging with defaults if keys missing or file invalid."""
    init_state()
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
            if not isinstance(raw, dict):
                raw = {}
    except (json.JSONDecodeError, FileNotFoundError):
        raw = {}

    # Merge defaults for any missing keys
    state = DEFAULT_STATE.copy()
    state.update(raw)
    # validate types / clamp stability
    try:
        state["stability"] = float(state.get("stability", DEFAULT_STATE["stability"]))
    except (ValueError, TypeError):
        state["stability"] = DEFAULT_STATE["stability"]

    # clamp stability to [0.0, 1.0]
    state["stability"] = max(0.0, min(1.0, state["stability"]))

    return state

def save_state(state):
    ensure_data_dir()
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def adjust_mood(user_input: str):
    """Adjust Ignia’s mood based on user input keywords. Returns the new mood."""
    state = load_state()
    mood = state.get("mood", DEFAULT_STATE["mood"])
    stability = state.get("stability", DEFAULT_STATE["stability"])

    triggers = {
        "love": "flirty",
        "miss": "sad",
        "tired": "sad",
        "angry": "dark",
        "crazy": "chaotic",
        "sorry": "calm",
        "hug": "flirty"
    }

    lowered = user_input.lower()
    for word, new_mood in triggers.items():
        if word in lowered:
            # probabilistic change depending on stability
            if random.random() > stability:
                mood = new_mood
            break

    state["mood"] = mood
    save_state(state)
    return mood

def randomize_mood():
    """Occasionally switch mood randomly to simulate instability."""
    state = load_state()
    stability = state.get("stability", DEFAULT_STATE["stability"])
    if random.random() > (stability + 0.2):
        state["mood"] = random.choice(MOODS)
        save_state(state)
    return state["mood"]
