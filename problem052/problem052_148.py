from itertools import accumulate, repeat, takewhile
(lambda n:
    (lambda include3:
        print('',
              *filter(None,
                      map(lambda i: i if i % 3 == 0 else include3(i),
                          range(1, n+1)))))(
        (lambda x:
            next(map(lambda _: x,
                     filter(lambda d: d % 10 == 3,
                            takewhile(bool,
                                      accumulate(repeat(x),
                                                 lambda a, _: a // 10)))),
                 None))))(int(input()))