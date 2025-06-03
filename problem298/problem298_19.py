def actual(n, k, h_list):
    return len([h for h in h_list if h >= k])

n, k = map(int, input().split())
h_list = map(int, input().split())

print(actual(n, k, h_list))