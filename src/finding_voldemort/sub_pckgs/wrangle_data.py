''''functions to help with data wrangling'''
def rm_short_wrds(wrd_lst: list, num: int =2) -> None:
    '''takes a list of words and removes words with length <= num'''
    for wrd in wrd_lst[:]:
        if len(wrd) > num:
            wrd_lst.remove(wrd)

