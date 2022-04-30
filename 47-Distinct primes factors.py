# import itertools, math
#
#
# def compute():
#     cond = lambda i: all((count_distinct_prime_factors(i + j) == 4) for j in range(4))
#     ans = next(filter(cond, itertools.count()))
#     return str(ans)
#
#
# def count_distinct_prime_factors(n):
#     count = 0
#     while n > 1:
#         count += 1
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 while True:
#                     n //= i
#                     if n % i != 0:
#                         break
#                 break
#         else:
#             break  # n is prime
#     return count
#
#
# if __name__ == "__main__":
#     print(compute())

#################################################################
def prime_factors(x):
    bolen = 2
    bolenler = set()

    while bolen < x ** 0.5:
        if x % bolen == 0:
            while True:
                bolenler.add(bolen)
                x //= bolen
                if x % bolen != 0:
                    break

            # bolenler.add(bolen)
            # x //= bolen
            # bolen -= 1

        bolen += 1

    return len(bolenler) + 1


number = 2 * 3 * 5 * 7

while True:
    flag = True
    for i in range(4):
        if prime_factors(number + i) != 4:
            flag = False
            break
    if flag:
        print(number)
        break

    number += 1
