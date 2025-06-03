import itertools


n_even, n_odd = map(int, input().split())

# nC2 なので、combinations使わなくてもいいと思う
count1 = n_even * (n_even - 1) // 2
count2 = n_odd * (n_odd - 1) // 2

print(count1 + count2)

# itertools.combinations を使ってもOK
count1 = len(list(itertools.combinations(range(n_even), r=2)))
count2 = len(list(itertools.combinations(range(n_odd), r=2)))

