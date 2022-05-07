def compute():
    numerator = 1
    denominator = 2
    res = 0
    for _ in range(1, 1000):
        numerator, denominator = denominator, 2 * denominator + numerator
        if len(str(numerator + denominator)) > len(str(denominator)):
            res += 1

    print(res)


compute()
