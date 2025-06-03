from functools import reduce
rpn = lambda s: int(reduce(
    lambda x, y: (
        x[:-2] + [str(eval(x[-2]+y[0]+x[-1]))] if y in '+-*'
        else x + [y]
    ), s.split(), []
)[0])
print(rpn(input()))

