'''main program for finding voldemort'''
import sys
from finding_voldemort import sub_pckgs.import_gloss as ig

# ==========================================
# INPUTS:

GLOSS_FILE = 'engmix.txt'

# ==========================================

def enter_word() -> str:
    '''take a user input with text'''
    return input("Enter a word to search anagrams for")

def choose_word(choices: list) -> str:
    '''I: a list of choices,  | O: a word in the list or an empty string '''
    print('The following words can form anagrams: ',
          *choices, '\n')
    chosen_word = input('Enter a word or press enter to restart')
    if chosen_word in choices:
        return chosen_word
    return ''

def filter_gloss(glossary: list, word: str) -> list:
    '''filters a glossary to only include anagrams of word'''
    return [entry for entry in glossary if tuple(entry) in tuple(word)]

def anagram_is_finished(initial_word: str, chosen_anagrams: list) -> bool:
    '''check if complete word is contained in chosen_anagrams'''
    all_letters = ()
    for entry in chosen_anagrams:
        all_letters += tuple(entry)
    return all_letters == tuple(initial_word)

def anagram_impossible(anagram_lst) -> bool:
    '''check if there are anagrams left'''
    return len(anagram_lst) > 0

def print_finished(word:str, anagram: list) -> None:
    '''prints the finished anagram'''
    print(f'This is your anagram to {word}',
          *anagram, file=sys.stderr)

def main():
    '''main program'''
    while True:
        glossary = ig.import_gloss(GLOSS_FILE)
        word = enter_word()
        chosen_anagrams = []
        while not anagram_impossible(glossary):
            glossary = filter_gloss(glossary, word)
            chosen_word = choose_word(glossary)
            if not chosen_word:
                break
            chosen_anagrams.append(chosen_word)
            if anagram_is_finished(word, chosen_anagrams):
                print_finished(word, chosen_anagrams)
                break
        inp = input('Enter to play again, press "n" to quit')
        if inp == 'n':
            break


if __name__ == '__main__':
    main()
