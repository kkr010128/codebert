N = int(input())

result = {}
result["AC"] = 0
result["WA"] = 0
result["TLE"] = 0
result["RE"] = 0

for i in range(N):
    judge = input()
    result[judge] += 1

for key, value in result.items():
    print(f"{key} x {value}")