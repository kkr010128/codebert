n = int(input())
k = 0
num_list = [0] * 12

for i in range(12):
    num_list[i] = 26**(i+1)
    if n <= sum(num_list[:i]):
        k = i
        break
'print(num_list)'
'''print('k=' , k)'''
diff = n - (sum(num_list[:k-1]) + 1)
'''print(diff)'''
ans = ['a']*(k)
arr = [0] * (k)

for i in range(len(ans)):
    
    arr[i] = diff // 26**(len(ans)-1-i)%26

    '''print('arr = ',i,' ', arr[i])'''
    '''print('ans = ',i,' ', ord(ans[i]))'''
    ans[i] = (chr((ord(ans[i]) + arr[i])))
    

print(''.join(ans))