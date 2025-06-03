(lambda *_: None)(
    *map(print,
         map('Case {0[0]}: {0[1]}'.format,
             enumerate(iter(input, '0'), 1))))