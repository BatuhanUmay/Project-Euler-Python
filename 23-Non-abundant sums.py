
import math


def bolen_toplami(x):
    toplam = 1
    n = 2
    while n < math.ceil(math.sqrt(x)):
        if x % n == 0:
            toplam += n
            toplam += x // n
        n += 1

        if n * n == x:  # bizim sayımız tam kare ise örn:25
            toplam += n

    return toplam


def kontrolEbundant(x):
    return True if bolen_toplami(x) > x else False


abundants = list()
toplam = 0
sum_of_abundants = list()

for i in range(1, 28124):
    if kontrolEbundant(i):
        abundants.append(i)


sum_of_abundants = [0] * 28124

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] <= 28123:
            sum_of_abundants[abundants[i] + abundants[j]] = abundants[i] + abundants[j]

#0 olan indexlerin toplamı
for i in range(len(sum_of_abundants)):
    if sum_of_abundants[i] == 0:
        toplam += i

print(toplam)

###############################################################################

# def compute():
#     LIMIT = 28124
#     divisorsum = [0] * LIMIT
#     for i in range(1, LIMIT):
#         for j in range(i * 2, LIMIT, i):
#             divisorsum[j] += i
#     abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]
#
#     expressible = [False] * LIMIT
#     for i in abundantnums:
#         for j in abundantnums:
#             if i + j < LIMIT:
#                 expressible[i + j] = True
#             else:
#                 break
#
#     ans = sum(i for (i, x) in enumerate(expressible) if not x)
#     return str(ans)
#
#
# if __name__ == "__main__":
#     print(compute())
