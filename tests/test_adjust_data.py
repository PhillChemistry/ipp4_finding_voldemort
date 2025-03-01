'''test functions from wrangle_data module'''
from finding_voldemort.sub_pckgs import wrangle_data as wd

TEST_GLOSS = ['a', 'you', 'I', 'we', 'left']

def test_rm_short_wrds_fn_num_3():
    '''tests what happens if num is 3'''
    assert wd.rm_short_wrds(TEST_GLOSS, 3) == ['left']
