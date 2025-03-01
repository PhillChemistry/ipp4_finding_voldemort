'''tests contents of import_gloss.py'''

import finding_voldemort.sub_pckgs.import_gloss as ig

GLOSS_FILE = 'engmix.txt'
WRD = 'insert'

def test_import_gloss_fn_engmix_100_entries():
    '''checks against gloss'''
    glossary = ig.import_gloss(GLOSS_FILE)
    assert len(glossary) > 100

def test_import_gloss_fn_engmix_contains_wrd():
    '''checks if wrd in gloss'''
    assert WRD in ig.import_gloss(GLOSS_FILE)
