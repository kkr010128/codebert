#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
  values = []
  total = 0

  for _ in range(int(input())):
    s = input().strip()
    open_required = len(s)
    close_required = len(s)
    open_close = 0

    for i, c in enumerate(s):
      if c == '(':
        open_required = min(i, open_required)
        open_close += 1
      else:
        close_required = min(len(s) - i - 1, close_required)
        open_close -= 1

    total += open_close
    values.append([open_required, close_required, open_close, 0])

  if total != 0:
    print('No')
    return

  if len(values) > 500000:
    print('Yes')
    return

  fvals = values.copy()
  bvals = values

  fvals.sort(key=lambda x: (x[0], -x[2]))
  bvals.sort(key=lambda x: (x[1], x[2]))

  findex = 0
  bindex = 0

  while True:
    while findex < len(fvals) and fvals[findex][3] != 0:
      findex += 1

    while bindex < len(bvals) and bvals[bindex][3] != 0:
      bindex += 1

    if findex >= len(fvals) and bindex >= len(bvals):
      break

    fvals[findex][3] = 1
    bvals[bindex][3] = -1

  values = [v for v in fvals if v[3] == 1] + [v for v in bvals if v[3] == -1][::-1]

  open_close_f = 0
  open_close_b = 0

  for (oreq_f, _, ocval_f, _), (_, creq_b, ocval_b, _) in zip(values, values[::-1]):
    if oreq_f > open_close_f:
      print('No')
      return

    if creq_b > open_close_b:
      print('No')
      return

    open_close_f += ocval_f
    open_close_b -= ocval_b

  print('Yes')


if __name__ == '__main__':
  main()
