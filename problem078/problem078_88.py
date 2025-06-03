NUM = 1000000007

N = int(input())

all_colab = pow(10, N)
except_0or9_colab = pow(9, N)
except_0and9_colab = pow(8, N)

include_0and9_colab = all_colab - (2*except_0or9_colab - except_0and9_colab)

print(include_0and9_colab % NUM)