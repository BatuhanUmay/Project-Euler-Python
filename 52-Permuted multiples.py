# import itertools
#
#
# def multipleControl(n):
#
#     if digit_control(n, 2 * n) and digit_control(n, 3 * n) and \
#     digit_control(n, 4 * n) and digit_control(n, 5 * n) and \
#     digit_control(n, 6 * n):
#         return True
#
#     return False
#
#
# def digit_control(a, b):
#     a = str(a)
#     b = str(b)
#
#     if sorted(a) == sorted(b):
#         return int(a)
#
#
# for i in itertools.count(1):
#     if multipleControl(i):
#         print(i)
#         break

##########################################################

import itertools


def compute():
    cond = lambda i: all(sorted(str(i)) == sorted(str(i * j)) for j in range(2, 7))
    ans = next(i for i in itertools.count(1) if cond(i))
    return ans


if __name__ == "__main__":
    print(compute())
