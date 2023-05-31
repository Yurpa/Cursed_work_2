from utils.Functions import Censored

def test_Censored():
    assert Censored('Visa Gold 3589276410671603') == 'Visa Gold 3589 27** **** 1603'
