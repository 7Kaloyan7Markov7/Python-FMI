def spam(*args, **kwargs):
    result = {x : y for x,y in zip(args,kwargs.keys())}

    return result

print(spam(1,2,3,name1=4, name2=5, name3=6))
