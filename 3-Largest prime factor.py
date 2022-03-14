def isPrime(num):
    if num == 1:
        return False
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        return prime


primeList = []
num = 600851475143
for i in range(2, int(pow(num, 0.5)) + 1):
    if num % i == 0:
        if isPrime(i):
            primeList.append(i)

print(max(primeList))


#############################################################################################

# def calculate():
#     n = 600851475143
#
#     while True:
#         p = largestPrimeFactor(n)
#
#         if p < n:
#             n //= p
#         else:
#             return n
#
#
# def largestPrimeFactor(n):
#     assert n >= 2
#     for i in range(2, int(pow(num, 0.5)) + 1):
#         if n % i == 0:
#             return i
#     return n
#
#
# print(calculate())
