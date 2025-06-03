from itertools import starmap
(lambda *_: None)(
    *map(print,
         (lambda board, pairs: starmap(board, pairs))(
             (lambda h, w:
                 (lambda rows: ''.join(map(lambda i: rows[i%2], range(h))))(
                     (lambda row: (row[:w]+'\n', row[1:w+1]+'\n'))(
                         '#.'*(w//2+1)))),
             map(lambda t: map(int, t),
                 map(str.split, iter(input, '0 0'))))))