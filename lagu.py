import sys
import time


def play_lyrics():
    # Cuplikan lirik lagu "Perfect" - Ed Sheeran
    lines = [
        ("I found a love for me", 0.08),
        ("Darling, just dive right in and follow my lead", 0.08),
        ("Well, I found a girl, beautiful and sweet", 0.08),
        ("I never knew you were the someone waiting for me", 0.08),
    ]

    print("--- Perfect - Ed Sheeran ---\n")

    for line, char_delay in lines:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(1.2)  # Jeda antar baris


if __name__ == "__main__":
    play_lyrics()