# def is_pandigital(num, digit):
#     num = str(num)
#     unique = ""
#
#     ordered = "".join([str(i) for i in range(1, digit + 1)])
#
#     for i in num:
#         if i not in unique:
#             unique += i
#
#     return True if num == unique and "".join(sorted(num)) == ordered else False
#
#
# def seive_primes(n):
#     primesList = [True] * (n + 1)
#     primesList[0] = primesList[1] = False
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if primesList[i]:
#             for j in range(i * i, len(primesList), i):
#                 primesList[j] = False
#     return primesList
#
#
# primes = seive_primes(10 ** 7)
# maxi = 0
# for i in range(2, len(primes)):
#     if i > maxi and primes[i] and is_pandigital(i, len(str(i))):
#         maxi = i
#
# print(maxi)

######################################################

import itertools
import sympy

rakamlar = "1234567"
sayilar = list(itertools.permutations(rakamlar))

sayilar.sort(reverse=True)

for demet in sayilar:
    sayi = "".join(demet)

    if sympy.isprime(int(sayi)):
        print(sayi)
        break

######################################################

# import eulerlib
#
#
# def compute():
#     # Note: The only 1-digit pandigital number is 1, which is not prime. Thus we require n >= 2.
#     for n in reversed(range(2, 10)):
#         arr = list(reversed(range(1, n + 1)))
#         while True:
#             if arr[-1] not in NONPRIME_LAST_DIGITS:
#                 n = int("".join(str(x) for x in arr))
#                 if eulerlib.is_prime(n):
#                     return str(n)
#             if not prev_permutation(arr):
#                 break
#     raise AssertionError()
#
#
# NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}
#
#
# def prev_permutation(arr):
#     i = len(arr) - 1
#     while i > 0 and arr[i - 1] <= arr[i]:
#         i -= 1
#     if i <= 0:
#         return False
#     j = len(arr) - 1
#     while arr[j] >= arr[i - 1]:
#         j -= 1
#     arr[i - 1], arr[j] = arr[j], arr[i - 1]
#     arr[i:] = arr[len(arr) - 1: i - 1: -1]
#     return True
#
#
# if __name__ == "__main__":
#     print(compute())
