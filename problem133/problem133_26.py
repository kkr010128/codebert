from subprocess import run

with open("./tmp215378912379.cpp", mode='w') as f:
  f.write("""
#include <bits/stdc++.h>
template <class T>
concept Integral = std::is_integral_v<T>;

int main() {
  auto f = []<Integral T>(T a, T b) { return a * b; };
  int a, b;
  std::cin >> a >> b;
  std::cout << f(a, b) << std::endl;
}
""")

run("g++ -o ./tmp215378912379 -std=gnu++2a -fconcepts ./tmp215378912379.cpp && ./tmp215378912379", shell=True)