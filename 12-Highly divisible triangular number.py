import math, itertools


def compute():
    triangle = 0
    for i in itertools.count(1):
        triangle += i
        if num_divisors(triangle) > 500:
            return triangle


def num_divisors(n):
    end = math.sqrt(n)
    result = sum(2
                 for i in range(1, int(math.sqrt(n)))
                 if n % i == 0)
    if end ** 2 == n:
        result -= 1
    return result


if __name__ == "__main__":
    print(compute())
