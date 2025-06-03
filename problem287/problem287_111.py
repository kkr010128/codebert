N = int(input())
def answer(N: int) -> str:
    x = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if N == i * j:
                x = 1
                return 'Yes'
    if x == 0:
        return 'No'
print(answer(N))