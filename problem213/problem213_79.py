def resolve():
  N = int(input())
  X = [int(x) for x in input().split(" ")]
  min_X = min(X)
  max_X = max(X)
  # sigma(Xi-P) = X**2 - 2*Xi*P + P**2
  sum_of_x = sum(X)

  sum_of_squared = 0
  for x in X:
    sum_of_squared += x**2

  temp_sum_of_cost = sum_of_squared - 2 * min_X * sum_of_x + N * min_X**2
  for p in range(min_X, max_X+1):
    sum_of_cost = sum_of_squared - 2 * p * sum_of_x + N * p**2
    if sum_of_cost < temp_sum_of_cost:
      temp_sum_of_cost = sum_of_cost

  print(temp_sum_of_cost)

if __name__ == "__main__":
  resolve()