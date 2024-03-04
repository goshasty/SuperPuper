from typing import Tuple, List
import random

def bullscows(guess: str, secret: str) -> Tuple[int, int]:
    bulls = 0
    for secret_letter, guess_letter in zip(secret, guess):
        bulls += secret_letter == guess_letter
    
    cows = 0
    for guess_letter in guess:
        cows += guess_letter in secret
    return (bulls, cows-bulls)

def ask(prompt: str, valid: List[str] = None) -> str:
    return 'ропот'

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def gameplay(ask: callable, inform: callable, words: List[str]) -> int:
    secret = random.choice(words)
    guess = ask("Введите слово: ", words)
    bulls, cows = bullscows(guess, secret)
    inform("Быки: {}, Коровы: {}", bulls, cows)
    return True

print(gameplay(ask, inform, ['полип']))

