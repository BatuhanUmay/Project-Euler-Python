def is_prime():
    # Sieve of Eratosthenes
    control = [True] * 1000000  # 0 1 2 3 ... 999999
    control[0] = control[1] = False

    for i in range(2, int(pow(1000000, 0.5) + 1)):
        if control[i]:
            for j in range(i * i, len(control), i):
                control[j] = False

    return control


def compute():
    primeList = is_prime()

    def is_circular_prime(n):
        s = str(n)
        return all(primeList[int(s[i:] + s[:i])] for i in range(len(s)))

    ans = sum(1
              for i in range(len(primeList))
              if is_circular_prime(i)
              )
    return ans


print(compute())
