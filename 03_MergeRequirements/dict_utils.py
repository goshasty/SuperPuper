import os
from typing import List
import urllib
from urllib.parse import urlparse
import urllib.request
from pathlib import Path



def download_words(url):
    DICT_PATH = "dictionaries/"
    DICT_FILENAME = "words.txt"
    
    DICT_FULL_PATH = Path(DICT_PATH, DICT_FILENAME)
    p = Path(DICT_PATH)
    p.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, DICT_FULL_PATH)
    
    return DICT_FULL_PATH


def is_valid_url(url_candidate: str) -> bool:
    parsed_url = urlparse(url_candidate)
    return bool(parsed_url.scheme)


def load_dict(dictionary: str) -> List[str]:
    if is_valid_url(dictionary):
        dictionary = download_words(dictionary)
    is_path = Path(dictionary).exists()
    if is_path:
        with open(dictionary, 'r') as fd:
            words = fd.read().splitlines()
            return words
    
    raise ValueError('dictionary is nor valid url neither path')
    
    
    