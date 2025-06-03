from itertools import starmap
(lambda *_: None)(
    *map(print,
         starmap(lambda h, w: ''.join(['#'*w + '\n'] +
                                      ['#' + '.'*(w-2) + '#\n'] * (h-2) +
                                      ['#'*w + '\n']),
                 map(lambda ss: map(int, ss),
                     map(str.split, iter(input, '0 0'))))))