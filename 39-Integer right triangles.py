def right_triangle():
    maxSol = {}

    for p in range(1, 1001):
        counter = 0
        for a in range(1, p + 1):
            for b in range(a, (p - a) // 2 + 1):
                c = p - (a + b)
                if a * a + b * b == c * c:
                    counter += 1

        maxSol[p] = counter

    maxValue = max(maxSol, key=maxSol.get)
    return maxValue


print(right_triangle())

##########################################################################

# def compute():
#     ans = max(range(1, 1001), key=count_solutions)
#     return str(ans)
#
#
# def count_solutions(p):
#     result = 0
#     for a in range(1, p + 1):
#         for b in range(a, (p - a) // 2 + 1):
#             c = p - a - b  # c >= b
#             if a * a + b * b == c * c:
#                 result += 1
#     return result
#
#
# if __name__ == "__main__":
#     print(compute())
