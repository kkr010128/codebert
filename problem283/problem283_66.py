def solution(N):
    ans = 0
    for i in range(N-1, int(N/2), -1):
        j = N-i
        ans+=1
    return ans

test_input = input()
test_input = int(test_input)
print(solution(test_input))