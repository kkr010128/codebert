import math

def main():
  t1, t2 = map(int, input().split())
  a1, a2 = map(int, input().split())
  b1, b2 = map(int, input().split())

  sumA = t1 * a1 + t2 * a2
  sumB = t1 * b1 + t2 * b2

  if sumA == sumB:
    return 'infinity'
  if sumA < sumB:
    sumA, sumB = sumB, sumA
    a1, b1 = b1, a1
    a2, b2 = b2, a2
  # A の方が sum が大きいとする

  halfA = t1 * a1
  halfB = t1 * b1
  if halfA > halfB:
    return 0
  div, mod = divmod(halfB - halfA, sumA - sumB)
  if mod == 0:
    return div * 2
  return div * 2 + 1

print(main())