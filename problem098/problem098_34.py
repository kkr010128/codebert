N = int(input())
C = input()
answer = 0

for i in range(N):
    if C[i] == 'W':
        red_start = i
        break
    if i == N-1:
        red_start = N-1

for i in range(1, N+1):
    if C[-i] == 'R':
        white_start = i
        break
    if i == N:
        white_start = N

red_pos = red_start
white_pos = white_start    

while red_pos + white_pos < N:
    answer += 1
    for i in range(red_pos+1, N):
        if C[i] == 'W':
            red_pos = i
            break
        if i == N-1:
            red_pos = N-1
    for i in range(white_pos+1, N+1):
        if C[-i] == 'R':
            white_pos = i
            break
        if i == N:
            white_pos = N

print(answer)