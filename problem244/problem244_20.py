inputted = list(map(int, input().split()))
K = inputted[0]
X = inputted[1]

total = 500 * K;
answer = 'Yes' if total >= X else 'No';

print(answer);
