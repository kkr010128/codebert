import sys
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H1, M1, H2, M2, K = map(int, read().split())

hr = (H2- H1) * 60 
if M2 >= M1:
    _min = M2 - M1
    hr = (H2- H1) * 60 
    ans = hr + _min
else:
    _min = (M2 + 60) - M1
    hr = (H2- H1 -1) * 60 
    ans = hr + _min

print(ans - K)