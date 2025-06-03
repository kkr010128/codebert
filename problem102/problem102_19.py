n,k = map(int, input().split())

a_list = list(map(int, input().split()))

for i in range(len(a_list)):
    if i+k > len(a_list)-1:
        break
    if a_list[i] < a_list[i+k]:
        print("Yes")
    else:
        print("No")