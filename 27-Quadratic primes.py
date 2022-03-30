# import itertools
#
#
# def compute():
#     ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)), key=count_consecutive_primes)
#     return ans[0] * ans[1]
#
#
# def count_consecutive_primes(ab):
#     a, b = ab
#
#     for i in itertools.count():
#         n = i * i + i * a + b
#         if not is_prime(n):
#             return i
#
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(pow(num, 0.5) + 1), 2):
#             if num % i == 0:
#                 return False
#         return True
#
#
# def list_primality(n):
#     result = [True] * (n + 1)
#     result[0] = result[1] = False
#     for i in range(int(pow(n, 0.5) + 1)):
#         if result[i]:
#             for j in range(i * i, len(result), i):
#                 result[j] = False
#     return result
#
#
# isPrimeCache = list_primality(1000)
#
#
# def isPrime(n):
#     if n < 0:
#         return False
#     elif n < len(isPrimeCache):
#         return isPrimeCache[n]
#     else:
#         return is_prime(n)
#
#
# if __name__ == "__main__":
#     print(compute())

#############################################################################

import sympy

prime_count = 0

for a in range(-1000, 1000):
    for b in sympy.primerange(1, 1000):
        aux_prime_count = 0
        n = 0
        while sympy.isprime(n ** 2 + a * n + b):
            aux_prime_count += 1
            n += 1
        if aux_prime_count > prime_count:
            prime_count = aux_prime_count
            a_max = a
            b_max = b

print(a_max)
print(b_max)
print(a_max * b_max)
print(prime_count)
