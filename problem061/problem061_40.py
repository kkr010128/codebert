def transform(c):
    if type(c) is str:
        if c.isupper():
            return c.lower()
        else:
            return c.upper()
    else:
        return c
    
print("".join(map(lambda c: transform(c), input())))