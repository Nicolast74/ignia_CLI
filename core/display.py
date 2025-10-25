import sys
import time
import random
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text

console = Console()

def typing_effect(text: str, delay: float = 0.02, min_delay: float = 0.01, max_delay: float = 0.03):
    """Simulate typing effect for more immersive experience"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
    sys.stdout.write("\n")
    sys.stdout.flush()

def display_message(role: str, message: str, mood_color: str = "white"):
    """Show message with role-based styling"""
    name = "Ignia ❤️" if role == "assistant" else "You"
    color = mood_color if role == "assistant" else "cyan"
    console.print(f"[bold {color}]{name}:[/bold {color}] {message}")

def show_markdown(md_text: str):
    """Render Markdown for formatted outputs"""
    md = Markdown(md_text)
    console.print(md)

def show_typing(name: str = "Ignia"):
    """Display typing indicator"""
    console.print(f"[dim]{name} is typing...[/dim]", end="\r")
    time.sleep(random.uniform(0.8, 1.5))
    console.print(" " * 30, end="\r")  # clear line

def display_system_message(msg: str):
    """System-level messages (for warnings/info)"""
    console.print(f"[bold yellow][!][/bold yellow] {msg}")
