N, A, B=map(int, input().split(" "))

result=A*(N//(A+B))+min(N%(A+B), A)

print(result)