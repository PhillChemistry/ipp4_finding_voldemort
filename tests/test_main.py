'''únit tests for main'''
import builtins
import finding_voldemort.main as m

NAME = 'Voldemort'
CHOICES = ['word1', 'word2', 'word3']
GLOSS = ['volde', 'mort', 'v', 'xyz', 'zzz']

#enter_word():
def test_enter_word(monkeypatch):
    ''''tests fn with monkeypatch'''
    def mock_fn(display_text):
        print(display_text)
        return NAME

    monkeypatch.setattr(builtins, 'input', mock_fn)
    assert m.enter_word() == NAME
   

#choose_word():
def test_choose_word_fn_reduces_length(monkeypatch):
    '''tests if fn returns a word in the list'''
    choice = CHOICES[0]
    def mock_input(text):
        print(text)
        return choice
    monkeypatch.setattr(builtins, 'input', mock_input)
    assert m.choose_word(CHOICES) == choice

def test_choose_word_fn_wrong_choice(monkeypatch):
    '''tests fn if choice not in choices'''
    def mock_input(text):
        print(text)
        return 'not in choices'
    monkeypatch.setattr(builtins, 'input', mock_input)
    assert m.choose_word(CHOICES) == ''


#filter_gloss():
def test_filter_gloss_fn_mock_gloss():
    '''fn returns correct results for 1 word'''
    assert 'volde' in m.filter_gloss(GLOSS, NAME)


def test_filter_gloss_fn_contains_all():
    '''fn contains all results in mock dictionary'''
    assert m.filter_gloss(GLOSS, NAME) == ['volde', 'mort', 'v']


def test_filter_gloss_fn_does_not_return_incorrect():
    '''fn doesn't return incorrect words'''
    filtered_gloss = m.filter_gloss(GLOSS, NAME)
    assert not GLOSS[3] in filtered_gloss and not GLOSS[4] in filtered_gloss


#anagram_is_finished:
def test_anagram_is_finished_true():
    '''fn returns true when the anagram is finished'''
    assert m.anagram_is_finished(NAME, CHOICES[:2])


def test_anagram_is_finished_false():
    '''fn returns false if not finished'''
    assert not m.anagram_is_finished(NAME, [''])


#anagram_impossible:
def test_anagram_is_impossible_empty_gloss():
    '''fn returns true if glossary is empty'''
    assert  m.anagram_impossible([])


def test_anagram_impossible_not_true():
    '''fn returns false if gloss contains words'''
    assert not m.anagram_impossible(CHOICES)

#print_finished:
def test_print_finished_correct_format(capsys):
    ''''fn returns correct format'''
    m.print_finished(NAME, GLOSS[:2])
    capture = capsys.readouterr()
    assert capture.out == \
            'This is your anagram to Voldemort:\nvolde, mort\n'