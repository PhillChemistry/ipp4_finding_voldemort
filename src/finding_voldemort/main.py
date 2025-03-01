'''main program for finding voldemort'''
import sys
import finding_voldemort.sub_pckgs.import_gloss as ig

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


def filter_gloss(glossary: list, char_lst: list) -> list:
    '''filters a glossary to only include anagrams of word'''
    return [entry for entry in glossary if list(entry) in char_lst]


def anagram_is_finished(initial_word: str, chosen_anagrams: list) -> bool:
    '''check if complete word is contained in chosen_anagrams'''
    all_letters = ()
    for entry in chosen_anagrams:
        all_letters += tuple(entry)
    return all_letters == tuple(initial_word)


def anagram_impossible(anagram_lst) -> bool:
    '''check if there are anagrams left'''
    return len(anagram_lst) > 0


def reduce_remaining_word(wrd_char_lst: list, chosen_word: str) -> list:
    '''I: list of chars forming a target word, a word as a string |
    O: a new, wrd_char_lst'''
    char_lst = list(chosen_word)
    for char in char_lst:
        wrd_char_lst.remove(char)


def print_finished(word:str, anagram: list) -> None:
    '''prints the finished anagram'''
    print(f'This is your anagram to {word}:')
    print(', '.join(anagram))


def main():
    '''main program'''
    while True:
        glossary = ig.import_gloss(GLOSS_FILE)
        word = enter_word()
        remaining_word = list(word)
        chosen_anagrams = []
        while not anagram_impossible(glossary):
            glossary = filter_gloss(glossary, remaining_word)
            chosen_word = choose_word(glossary)
            reduce_remaining_word(remaining_word, chosen_word)
            #reduce_remaining_word(remaining_word, chosen_word)
            if not chosen_word:  # input is not in glossary
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
