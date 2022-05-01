def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True


def sieve(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def compute():
    LIMIT = 10000
    is_prime = sieve(LIMIT - 1)

    for base in range(1000, LIMIT):
        if is_prime[base]:
            for step in range(1, LIMIT):
                a = base + step
                b = a + step
                if a < LIMIT and is_prime[a] and has_same_digits(a, base) \
                        and b < LIMIT and is_prime[b] and has_same_digits(b, base) \
                        and (base != 1487 or a != 4817):
                    return str(base) + str(a) + str(b)

    raise RuntimeError("Not found")


def has_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))


if __name__ == "__main__":
    print(compute())
