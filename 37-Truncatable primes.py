import itertools


def is_prime(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True

    else:
        for i in range(2, int(pow(x, 0.5)) + 1):
            if x % i == 0:
                return False
        return True


def is_truncatable_prime(n):
    # n = 3797, 797, 97, 7 left-truncatable
    i = 10
    while i <= n:
        if not is_prime(n % i):
            return False
        i *= 10

    # n = 3797, 379, 37, 3 right-truncatable
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True


def compute():
    ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
    return ans

    # count = 0
    # num = 10
    # res = 0
    #
    # while count != 11:
    #     if is_truncatable_prime(num):
    #         res += num
    #         count += 1
    #
    #     num += 1
    #
    # return res


if __name__ == "__main__":
    print(compute())
