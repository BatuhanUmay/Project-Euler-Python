# nums = ""
# res = 1
#
# for i in range(1, 1000000):
#     nums += str(i)
#
#
# print(int(nums[0]) * int(nums[9]) * int(nums[99]) * int(nums[999]) * int(nums[9999]) * int(nums[99999]) * int(
#     nums[999999]))
#####################################################################

def compute():
    s = "".join(str(i) for i in range(1, 1000000))
    ans = 1
    for i in range(7):
        ans *= int(s[10 ** i - 1])
    return ans


if __name__ == "__main__":
    print(compute())
