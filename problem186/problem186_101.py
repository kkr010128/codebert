k , n= map(int, input().split())
a_list = list(map(int, input().split()))
diff_list = []
for i in range(n-1):
    diff_list.append(a_list[i+1]- a_list[i])
diff_list.append(k-a_list[n-1] + a_list[0])
print(sum(diff_list)-max(diff_list))