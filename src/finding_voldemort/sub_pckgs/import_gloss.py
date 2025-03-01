'''Allows importing a glossary'''
from pathlib import Path

def import_gloss(file_name: str) -> list:
    '''import a glossary; I: file_name | O: glossary list'''
    dir_path = Path(__file__).parents[3].resolve()
    file_path = dir_path / "data" / file_name
    try:
        with open(file_path, encoding='utf-8', errors='ignore'):
            gloss = file_path.read_text(
                encoding='utf-8',errors='ignore').strip().lower().splitlines()
    except IOError as e:
        print(e, f"\nDid not find folder {file_path}")
        raise e
    return gloss