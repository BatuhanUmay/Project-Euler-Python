def TheSumOfTheSquares(n):
    res = n * (n + 1) * (2 * n + 1) // 6
    return res


def TheSquareOfTheSum(n):
    res = n * (n + 1) // 2
    return res ** 2


print(TheSquareOfTheSum(100) - TheSumOfTheSquares(100))

#############################################################################################


# def compute():
# 	N = 100
# 	s = sum(i for i in range(1, N + 1))
# 	s2 = sum(i**2 for i in range(1, N + 1))
# 	return str(s**2 - s2)
#
#
# if __name__ == "__main__":
# 	print(compute())
