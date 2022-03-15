# x * y = obeb(x, y) * okek(x, y)
# LCM(x, y) = x * y / GCD(x, y).
# gcd = obeb
# lcm = okek

# def obeb(x, y):
#     obeb = 1
#     bolen = 1
#     while bolen < min(x, y) + 1:
#         if x % bolen == 0 and y % bolen == 0:
#             obeb = bolen
#         bolen += 1
#     return obeb
# 
# def okek(x, y):
#     return (x * y) / obeb(x, y)
# 
# def solution():
#     res = 1
#     for i in range(1, 21):
#         res *= i // obeb(i, res)
# 
#     return res
# 
# 
# print(solution())
#############################################################################################

import math
import functools

def obeb_GCD(x, y):
    return math.gcd(x, y)

def okek_LCM(x, y):
    return (x * y) // obeb_GCD(x, y) 

liste = range(1, 21)
print(functools.reduce(okek_LCM, liste))

#############################################################################################
# import math
# def compute():
#     ans = 1
#     for i in range(1, 21):
#         ans *= i // math.gcd(i, ans)
#     return str(ans)
#
#
# if __name__ == "__main__":
#     print(compute())
