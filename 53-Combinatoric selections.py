import math


def combi(n, r):
    return int((math.factorial(n)) / (math.factorial(r) * math.factorial(n - r)))


count = sum(1
            for i in range(1, 101)
            for j in range(1, i)
            if combi(i, j) > 1000000)

print(count)
