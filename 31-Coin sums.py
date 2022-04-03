def compute():
    TOTAL = 200
    ways = [1] + [0] * TOTAL

    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]

    return ways[-1]


if __name__ == "__main__":
    print(compute())

###########################################################################

# counter = 0
# for x in range(2):  # x => 2£ == 200p yani max 2 tane kullanabiliriz
#     for a in range(3):  # a => 1£ == 100p yani max 3 tane kullanabiliriz
#         if 200 * x + 100 * a > 200:
#             break
#         for b in range(5):  # 50p
#             if 200 * x + 100 * a + 50 * b > 200:
#                 break
#             for c in range(11):  # 20p
#                 if 200 * x + 100 * a + 50 * b + 20 * c > 200:
#                     break
#                 for d in range(21):  # 10p
#                     if 200 * x + 100 * a + 50 * b + 20 * c + 10 * d > 200:
#                         break
#                     for e in range(41):  # 5p
#                         if 200 * x + 100 * a + 50 * b + 20 * c + 10 * d + 5 * e > 200:
#                             break
#                         for f in range(101):  # 2p
#                             if 200 * x + 100 * a + 50 * b + 20 * c + 10 * d + 5 * e + 2 * f <= 200:
#                                 counter += 1
#
# print(counter)
