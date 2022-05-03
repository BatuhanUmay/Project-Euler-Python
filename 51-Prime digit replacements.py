from sympy import sieve
from sympy import isprime


def repeat_count(num):
    digits = dict()
    num = str(num)
    for digit in num:
        if digit in digits:
            digits[digit] += 1
        else:
            digits[digit] = 1

    digit_counts = []
    for digit, count in digits.items():
        digit_counts.append([digit, count])

    return digit_counts


def make_family(num):
    num = str(num)
    families = []
    # repeats = [i[0] for i in repeat_count(int(num))]
    repeats = [i[0] for i in repeat_count(int(num)) if i[1] == 3]
    for i in repeats:
        family = []
        for j in range(10):
            replaced = num.replace(i, str(j))
            if isprime(int(replaced)) and replaced[0] != '0':
                family.append(int(replaced))
        families.append(family)
    return families


primes = list(sieve.primerange(10 ** 5, 10 ** 6))

done = False
for i in primes:
    if done:
        break
    families = make_family(i)
    for j in families:
        if len(j) == 8:
            print(min(j))
            done = True
            break

##############################################################

# import eulerlib
#
#
# def compute():
#     isprime = eulerlib.list_primality(1000000)
#     for i in range(len(isprime)):
#         if not isprime[i]:
#             continue
#
#         n = [int(c) for c in str(i)]
#         for mask in range(1 << len(n)):
#             digits = do_mask(n, mask)
#             count = 0
#             for j in range(10):
#                 if digits[0] != 0 and isprime[to_number(digits)]:
#                     count += 1
#                 digits = add_mask(digits, mask)
#
#             if count == 8:
#                 digits = do_mask(n, mask)
#                 for j in range(10):
#                     if digits[0] != 0 and isprime[to_number(digits)]:
#                         return str(to_number(digits))
#                     digits = add_mask(digits, mask)
#     raise AssertionError("Not found")
#
#
# def do_mask(digits, mask):
#     return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]
#
#
# def add_mask(digits, mask):
#     return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]
#
#
# def to_number(digits):
#     result = 0
#     for d in digits:
#         result = result * 10 + d
#     return result
#
#
# if __name__ == "__main__":
#     print(compute())
