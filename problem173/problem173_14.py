# FizzBuzz Sum
N = int(input())
ans = ((1+N) * N)/2 - ((3 + 3*(N//3)) * (N//3))/2 - ((5 + 5*(N//5)) * (N//5))/2 + ((15 + 15*(N//15)) * (N//15))/2
print(int(ans))