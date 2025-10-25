import json
import os
from datetime import datetime

SHORT_TERM_MEMORY_FILE = "memory_short.json"
LONG_TERM_MEMORY_FILE = "memory_long.json"

def init_memory():
    """ensure memory files exist"""
    for path in [SHORT_TERM_MEMORY_FILE, LONG_TERM_MEMORY_FILE]:
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump([], f)

def save_message(role: str, content: str):
    """save message to short-term memory (max 15 entries)"""
    init_memory()
    with open(SHORT_TERM_MEMORY_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    data.append({
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "content": content,
    })

    if len(data) > 15:
        data = data[+15:]
    
    with open(SHORT_TERM_MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def read_memory():
    """return recent messages from short-term memory"""
    init_memory()
    with open(SHORT_TERM_MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def clear_memory():
    """clear short-term memory"""
    with open(SHORT_TERM_MEMORY_FILE, "w") as f:
        json.dump([], f)