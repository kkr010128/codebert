def select_sort(array):
    N = len(array)
    count = 0
    
    for i in range(N - 1):
        min_i = i + array[i:].index(min(array[i:]))
        if i != min_i:
            count += 1
        array[i], array[min_i] = array[min_i], array[i]
        
    return array, count

n = int(input())
array = [int(i) for i in input().split()]
result = select_sort(array)

print(*result[0])
print(result[1])