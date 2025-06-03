n, k = map(int, input().split())

w = []

for i in range(n):
    w.append(int(input()))
   
def carriable(P, n, k, w):
    j = 0
    for i in range(k):
        sum = 0
        while j < n and sum + w[j] <= P:
            sum += w[j]
            j += 1
    return j

def binary_search(p_left, p_right, n, k, w):
    if p_left == p_right:
        return p_left
    else:
        p_center = (p_left + p_right)//2
        # because we have to search for the smallest p which satisfies carriable(p, n, k, w) = n, 
        # be careful of the inequality condition
        if carriable(p_center, n, k, w) >= n:
            return binary_search(p_left, p_center, n, k, w)
        else:
            return binary_search(p_center + 1, p_right, n, k, w)

p_left = 0
p_right = sum(w)
print(binary_search(p_left, p_right, n, k, w))
