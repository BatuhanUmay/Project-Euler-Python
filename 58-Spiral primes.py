# From the diagram, let's observe the four corners of an n * n square (where n is odd).
# It's not hard to convince yourself that:
# - The bottom right corner always has the value n^2.
# Working clockwise (backwards):
# - The bottom left corner has the value n^2 - (n - 1).
# - The top left corner has the value n^2 - 2(n - 1).
# - The top right has the value n^2 - 3(n - 1).
# Furthermore, the number of elements on the diagonal is 2n - 1.

import fractions, itertools, math


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


def compute():
    TARGET = fractions.Fraction(1, 10)
    num_primes = 0

    for n in itertools.count(1, 2): # 1, 3, 5, 7, ...
        for i in range(4):
            if is_prime(n * n - i * (n - 1)):
                num_primes += 1

        if n > 1 and fractions.Fraction(num_primes, n * 2 - 1) < TARGET:
            return n


if __name__ == "__main__":
    print(compute())
