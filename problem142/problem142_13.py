"""AtCoder."""

n = int(input()[-1])

s = None

if n in (2, 4, 5, 7, 9):
    s = 'hon'
elif n in (0, 1, 6, 8):
    s = 'pon'
elif n in (3,):
    s = 'bon'

print(s)
