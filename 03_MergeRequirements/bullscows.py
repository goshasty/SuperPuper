from typing import Tuple

def bullscows(guess: str, secret: str) -> Tuple[int, int]:
    bulls = 0
    for secret_letter, guess_letter in zip(secret, guess):
        bulls += secret_letter == guess_letter
    
    cows = 0
    for guess_letter in guess:
        cows += guess_letter in secret
    return (bulls, cows-bulls)

#print(bullscows("ропот", "полип"))

