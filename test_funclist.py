from funclist import list_of_letters


def test_list_of_letters():
    expected = list_of_letters(roster='fbmfbmbmmnmvmsvmsdmgiermgeoimgeimfgfkmgmmmmmnmnmnmnmmnmnmngfmkmhkgf')
    actual = list_of_letters(roster='fbmfbmbmmnmvmsvmsdmgiermgeoimgeimfgfkmgmmmmmnmnmnmnmmnmnmngfmkmhkgf')
    assert expected == actual
