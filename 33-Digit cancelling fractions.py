# import math
#
#
# def compute():
#     pay = 1
#     payda = 1
#
#     for denominator in range(10, 100):
#         for numerator in range(10, denominator):
#             n0 = numerator % 10
#             n1 = numerator // 10
#             d0 = denominator % 10
#             d1 = denominator // 10
#
#             if (n1 == d0 and n0 * denominator == numerator * d1) or \
#                     (n0 == d1 and n1 * denominator == numerator * d0):
#                 pay *= numerator
#                 payda *= denominator
#
#     return payda // math.gcd(pay, payda)
#
#
# if __name__ == "__main__":
#     print(compute())

#############################################################################

import math

ans = []

pay = 1
payda = 1

for i in range(10, 100):
    for j in range(i + 1, 100):
        if i % 10 == 0 or j % 10 == 0:
            continue

        stri = str(i)
        strj = str(j)

        if stri[1] == strj[0]:
            if int(stri[0]) / int(strj[1]) == i / j:
                ans.append(str(i) + "/" + str(j))
                pay *= i
                payda *= j
        elif stri[0] == strj[1]:
            if int(stri[1]) / int(strj[0]) == i / j:
                ans.append(str(i) + "/" + str(j))
                pay *= i
                payda *= j
        elif stri[0] == strj[0]:
            if int(stri[1]) / int(strj[1]) == i / j:
                ans.append(str(i) + "/" + str(j))
                pay *= i
                payda *= j
        elif stri[1] == strj[1]:
            if int(stri[0]) / int(strj[0]) == i / j:
                ans.append(str(i) + "/" + str(j))
                pay *= i
                payda *= j

print(ans)
print(payda // math.gcd(payda, pay))
