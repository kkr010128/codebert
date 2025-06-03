from functools import reduce
print(reduce(lambda a, b: 'a {} b'.format('<' if a < b else (
                                          '>' if a > b else '==')),
             map(int, input().split())))