# res = []
#
# for i in range(2, 1000000):
#     size = int(len(str(i)))
#     fifth_power = 0
#
#     for j in range(size):
#         fifth_power += int(str(i)[j]) ** 5
#
#     if fifth_power == i:
#         res.append(i)
#
# print(sum(res))

##############################################################################

def compute():
    res = sum(i
              for i in range(2, 1000000)
              if i == fifth_power_digit(i)
              )
    return res


def fifth_power_digit(num):
    return sum(int(i) ** 5 for i in str(num))


if __name__ == "__main__":
    print(compute())
