def sieve(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def list_primes(n):
    return [i for (i, isprime) in enumerate(sieve(n)) if isprime]


def compute():
    ans = 0
    isprime = sieve(999999)
    primes = list_primes(999999)
    consecutive = 0
    for i in range(len(primes)):
        sum = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            consec += 1
            if sum >= len(isprime):
                break
            if isprime[sum] and consec > consecutive:
                ans = sum
                consecutive = consec
    return str(ans)


if __name__ == "__main__":
    print(compute())
