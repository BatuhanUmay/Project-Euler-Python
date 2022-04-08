# def compute():
#     ans = ""
#
#     for n in range(2, 10):
#         for i in range(1, 10 ** (9 // n)):
#             s = "".join(str(i * j) for j in range(1, n + 1))
#             if "".join(sorted(s)) == "123456789":
#                 ans = max(s, ans)
#     return ans
#
#
# if __name__ == "__main__":
#     print(compute())


#######################################################################

myset = set("123456789")
pandigitals = []

for i in range(1, 10 ** 4):
    step = 1
    str_num = ""
    while True:
        number = i * step
        str_num += str(number)
        if len(str_num) >= 9:
            if len(str_num) > 9:
                break
            else:
                if set(str_num) == myset:
                    pandigitals.append(int(str_num))
                    break
        step += 1

print(max(pandigitals))
