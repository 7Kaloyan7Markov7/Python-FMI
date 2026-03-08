def spam(list, **kwargs):
    for key, value in kwargs.items():
        for string in list:
            if str(key) in string or str(value) in string:
                return True


    return False

print(spam(['asd', 'qwerty']))
print(spam(['asd', 'qwerty'], sd=1))
print(spam(['asd', 'qwerty'], qwerty=1))
print(spam(['asd', 'qwerty'], something='wer'))
