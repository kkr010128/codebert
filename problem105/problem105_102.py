my_range = int(input())
data_in = list(map(int,input().split()))
n_of_odd = 0
for ind in range(my_range):
  if (ind % 2) == 0:
    rem = data_in[ind] % 2
    n_of_odd = n_of_odd + rem
print(n_of_odd)