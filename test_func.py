from func import age_function


def test_age_function():
    expected_result = 'Invalid age value passed'
    age = -1
    actual_result = age_function(age)
    assert actual_result == expected_result


def test_age_function1():
    expected_result = 'The user is a child'
    age = 10
    actual_result = age_function(age)
    assert actual_result == expected_result


def test_age_function2():
    expected_result = 'you need to work'
    age = 30
    actual_result = age_function(age)
    assert actual_result == expected_result


def test_age_function3():
    expected_result = 'have a good old age'
    age = 90
    actual_result = age_function(age)
    assert actual_result == expected_result
