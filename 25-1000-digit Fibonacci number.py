def fibo(n):
    f1 = 1
    f2 = 1
    for _ in range(n - 2):
        f1, f2 = f2, f1 + f2

    return f2


i = 1
while True:
    if fibo(i):
        if len(str(fibo(i))) == 1000:
            print(i)
            break

        i += 1

############################################################################
# import itertools
#
#
# def compute():
#     DIGITS = 1000
#     prev = 1
#     cur = 0
#     for i in itertools.count():
#         if len(str(cur)) > DIGITS:
#             raise RuntimeError("Not found")
#         elif len(str(cur)) == DIGITS:
#             return str(i)
#
#         prev, cur = cur, prev + cur
#
#
# if __name__ == "__main__":
#     print(compute())
