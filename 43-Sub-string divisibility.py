# import itertools

# def pandigital_numbers():
#     nums = list(range(0, 10))
#     liste = itertools.permutations(nums)

#     return liste


# pandigitals = pandigital_numbers()
# res = 0

# for pan in pandigitals:

#     d2_d3_d4 = int(str(pan[1]) + str(pan[2]) + str(pan[3]))
#     d3_d4_d5 = int(str(pan[2]) + str(pan[3]) + str(pan[4]))
#     d4_d5_d6 = int(str(pan[3]) + str(pan[4]) + str(pan[5]))
#     d5_d6_d7 = int(str(pan[4]) + str(pan[5]) + str(pan[6]))
#     d6_d7_d8 = int(str(pan[5]) + str(pan[6]) + str(pan[7]))
#     d7_d8_d9 = int(str(pan[6]) + str(pan[7]) + str(pan[8]))
#     d8_d9_d10 = int(str(pan[7]) + str(pan[8]) + str(pan[9]))


#     if d2_d3_d4 % 2 == 0 and d3_d4_d5 % 3 == 0 and d4_d5_d6 % 5 == 0 and d5_d6_d7 % 7 == 0 and d6_d7_d8 % 11 == 0 and d7_d8_d9 % 13 == 0 and d8_d9_d10 % 17 == 0:
#         res += int(str(pan[0]) + str(pan[1]) + str(pan[2]) + str(pan[3]) + str(pan[4]) + str(pan[5]) + str(pan[6]) + str(pan[7]) + str(pan[8]) + str(pan[9]))

# print(res)

################################################

import itertools


def compute():
    ans = sum(
        int("".join(map(str, num)))
        for num in itertools.permutations(list(range(10)))
        if is_substring_divisible(num)
    )
    return ans


DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17]


def is_substring_divisible(num):
    return all(
        (num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
        for i, p in enumerate(DIVISIBILITY_TESTS))


if __name__ == "__main__":
    print(compute())
