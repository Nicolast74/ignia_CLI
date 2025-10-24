import time
import sys

def clean_input(text: str) -> str:
    return text.strip()

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
