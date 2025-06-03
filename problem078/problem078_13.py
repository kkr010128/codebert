seq = int(input())
a = int(10**9 + 7)
answer = (10**seq - 9**seq - 9**seq + 8**seq)%a
print(answer)