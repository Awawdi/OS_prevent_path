from pathlib import Path
import os

def is_valid(path_from_user : str) -> bool:

    try:
        return Path(path_from_user) != Path("/home/DoNotCopy")
    except OSError:
        return False
    

if __name__ == '__main__':
    path = input('please enter path to write the file ')
    file = 'orsan.txt'

    if is_valid(path):
        with open(file=str(Path(path)) + "/" + file, mode='w+', encoding="UTF-8") as f:
            f.write('Hello!')
    else:
        print(f'Invalid Path: {path}. Path should be 1) correct path and 2) not /home/DoNotCopy')
