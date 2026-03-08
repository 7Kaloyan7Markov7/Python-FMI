def spam(func):
    def wrapper(**kwargs):
        swapped = {value : key for key, value in kwargs.items()}
        return func(**swapped)

    return wrapper

@spam
def helper_fun(**kwargs):
    for key, value in kwargs.items():
        print(f"'{key}' passed with a value of '{value}'")

helper_fun(to_be_value='to_be_key')
