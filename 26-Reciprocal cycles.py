# import itertools
#
#
# def compute():
#     ans = max(range(1, 1000), key=reciprocal_cycle_len)
#     return ans
#
#
# def reciprocal_cycle_len(n):
#     seen = {}
#     x = 1
#     for i in itertools.count():
#         if x in seen:
#             return i - seen[x]
#         else:
#             seen[x] = i
#             x = x * 10 % n
#
#
# print(compute())

##############################################################################

max_devir = 0
bolen = 2

while bolen < 1000:
    bolunen = 1
    kalanlar = []

    while True:
        kalan = bolunen % bolen

        if kalan in kalanlar:
            first_index = kalanlar.index(kalan)
            last_index = len(kalanlar)

            if last_index - first_index > max_devir:
                max_devir = last_index - first_index
                aranan_sayi = bolen
            break

        bolunen = 10 * kalan
        kalanlar.append(kalan)

    bolen += 1

print("Devir tekrarı:", max_devir)
print("Aranan sayı:", aranan_sayi)
