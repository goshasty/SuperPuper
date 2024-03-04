from typing import Tuple, List
import random
import argparse
from dict_utils import load_dict, dictionary_only_length
from cowsay import cowsay, list_cows, read_dot_cow
from io import StringIO

def my_cow_say(message: str) -> str:
    with open("my.cow") as f:
        cowfile = read_dot_cow(f)
    return cowsay(message, cowfile=cowfile) + '\n'
    
def choose_cow() -> str:
    return random.choice(list_cows())

def ask(prompt: str, valid: List[str] = None) -> str:
    #print(cowsay(prompt, my_cow()))
    guess = input(my_cow_say(prompt))
    if valid:
        while guess not in valid:
            #print(cowsay('Слово не из словаря! '+ prompt, my_cow()))
            guess = input(my_cow_say(prompt))
    return guess

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay(format_string.format(bulls, cows), choose_cow()))

class BullCows:
    def __init__(self, ask: callable, inform: callable, words: List[str]):
        self.words = words
        self.secret = random.choice(words)
        self.ask = ask
        self.inform = inform
        self.num_tries = 0
        #print(self.secret)
    
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
        print('Поздравляю! Попыток потрачено попыток: {}'.format(self.num_tries))

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


def main(args):
    dictionary = args.dictionary[0]
    length = args.length
    words = load_dict(dictionary)
    if not length is None:
        words = dictionary_only_length(words, length)
    if not words:
        raise ValueError('no words with length: {}'.format(length))
    
    print('Возможных слов: {}'.format(len(words)))
    gameplay(ask, inform, words)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('dictionary', nargs=1)
    parser.add_argument('length', nargs='?', type=int)
    args = parser.parse_args()
    main(args)

