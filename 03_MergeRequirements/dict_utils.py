import os
from typing import List

def load_dict(dictionary: str) -> List[str]:
    is_path = os.path.exists(dictionary)
    if is_path:
        with open(dictionary, 'r') as fd:
            words = fd.read().splitlines()
    else:
        return []
    return words