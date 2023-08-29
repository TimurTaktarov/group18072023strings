from funclist import list_of_letters


def test_list_of_letters_one():
    expected = ['a', 'b']
    string_ = 'abmnm'
    actual = list_of_letters(string_)
    assert expected == actual


def test_list_of_letters_two():
    expected = []
    string_ = 'mnmmnmnm'
    actual = list_of_letters(string_)
    assert expected == actual


def test_list_of_letters_three():
    expected = []
    string_ = ''
    actual = list_of_letters(string_)
    assert expected == actual
