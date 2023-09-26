# decorator homework

def decorator_key_word_as_str(func):
    def operation_deco(*args, **kwargs):
        operation = func(*args, **kwargs)
        operation = str(operation)
        print(*args)
        print(kwargs)
        return operation

    return operation_deco


@decorator_key_word_as_str
def final_word(text1: str, text2: str) -> str:
    return text1 + text2


result = final_word(text1='при', text2='віт')
print(result)