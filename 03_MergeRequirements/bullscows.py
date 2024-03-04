from typing import Tuple, List
import random



def ask(prompt: str, valid: List[str] = None) -> str:
    quess = input()
    return quess

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

class BullCows:
    def __init__(self, ask: callable, inform: callable, words: List[str]):
        self.words = words
        self.secret = random.choice(words)
        self.ask = ask
        self.inform = inform
        
        self.num_tries = 0
    
    def bullscows(self, guess: str, secret: str) -> Tuple[int, int]:
        bulls = 0
        for secret_letter, guess_letter in zip(secret, guess):
            bulls += secret_letter == guess_letter
        
        cows = 0
        for guess_letter in guess:
            cows += guess_letter in secret
        return (bulls, cows-bulls)

    def is_guessed(self, bulls: int) -> bool:
        return bulls == len(self.secret)

    def end_game(self) -> None:
        print('Поздравляю! {}'.format(self.num_tries))

    def play(self) -> None:
        while True:
            self.num_tries += 1
            guess = self.ask("Введите слово: ", self.words)
            bulls, cows = self.bullscows(guess, self.secret)
            if self.is_guessed(bulls):
                self.end_game()
                break
            
            self.inform("Быки: {}, Коровы: {}", bulls, cows)

def gameplay(ask: callable, inform: callable, words: List[str]):
    game = BullCows(ask, inform, words)
    game.play()

if __name__ == '__main__':
    gameplay(ask, inform, ['полип'])

