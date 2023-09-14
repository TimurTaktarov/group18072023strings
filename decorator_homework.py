# decorator homework

def decorator_key_word_as_str(words):
    def operation_deco(*args):
        operation = words(*args)
        operation = str(operation)
        print(*args)
        return operation

    return operation_deco


@decorator_key_word_as_str
def final_word(text1: str, text2: str) -> str:
    return text1 + text2


result = final_word('при', 'віт')
print(result)
