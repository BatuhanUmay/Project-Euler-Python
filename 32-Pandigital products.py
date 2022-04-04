# import math
#
#
# def compute():
#     ans = sum(i for i in range(1, 10000) if pandigital_product(i))
#     return ans
#
#
# def pandigital_product(num):
#     for i in range(1, int(math.sqrt(num) + 1)):
#         if num % i == 0:
#             temp = str(num) + str(i) + str(num // i)
#             if "".join(sorted(temp)) == "123456789":
#                 return True
#
#     return False
#
#
# if __name__ == "__main__":
#     print(compute())

#############################################################################


import itertools

rakamlar = [*range(1, 10)]

permutations = list(itertools.permutations(rakamlar, 9))
result = set()

for number in permutations:
    # 2 basamaklı bir sayı * 3 basamaklı bir sayı = 4 basamaklı bir sayı
    sayi1 = number[0] * 10 + number[1]
    sayi2 = number[2] * 100 + number[3] * 10 + number[4]
    sayi3 = number[5] * 1000 + number[6] * 100 + number[7] * 10 + number[8]

    if sayi1 * sayi2 == sayi3:
        result.add(sayi3)

    # 1 basamaklı bir sayı * 4 basamaklı bir sayı = 4 basamaklı bir sayı
    sayi1 = number[0]
    sayi2 = number[1] * 1000 + number[2] * 100 + number[3] * 10 + number[4]
    sayi3 = number[5] * 1000 + number[6] * 100 + number[7] * 10 + number[8]

    if sayi1 * sayi2 == sayi3:
        result.add(sayi3)

print(sum(result))
