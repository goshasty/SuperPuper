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
    quess = input()
    return quess

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def is_guessed(bulls: int, secret: str) -> bool:
    return bulls == len(secret)

def end_game(num_tries: int) -> None:
     print('Поздравляю!'.format(num_tries))

def gameplay(ask: callable, inform: callable, words: List[str]) -> None:
    secret = random.choice(words)
    guessed = False
    num_tries = 0
    while guessed == False:
        num_tries += 1
        guess = ask("Введите слово: ", words)
        bulls, cows = bullscows(guess, secret)
        if is_guessed(bulls, secret):
            end_game(num_tries)
            break
        
        inform("Быки: {}, Коровы: {}", bulls, cows)

if __name__ == '__main__':
    gameplay(ask, inform, ['полип'])

