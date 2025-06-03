A = input()
B = input()

answer = [str(i) for i in range(1, 4)]

answer.remove(A)
answer.remove(B)
print(''.join(answer))
