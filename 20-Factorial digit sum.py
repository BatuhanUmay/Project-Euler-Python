# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * fact(num - 1)
#
#
# def digitSum(num):
#     num = str(num)
#     res = 0
#     for i in range(len(num)):
#         res += int(num[i])
#     return res
#
#
# def compute():
#     print(digitSum(fact(100)))
#
#
# if __name__ == "__main__":
#     compute()
##############################################################

import math

def compute():
    fact = math.factorial(100)
    res = sum(int(i) for i in str(fact))
    return res


if __name__ == "__main__":
	print(compute())
