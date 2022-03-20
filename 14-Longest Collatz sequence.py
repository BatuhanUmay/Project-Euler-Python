pastNum = dict()


def collatz(num, pastNum):
    given = num
    steps = 1

    while num != 1:
        if num in pastNum:
            steps += pastNum[num] - 1
            break

        if num % 2 == 0:
            num //= 2
            steps += 1
        else:
            num = num * 3 + 1
            steps += 1

    pastNum[given] = steps
    return steps


count = 0
wanted = 0

for num in range(1, 1000001):
    moveCount = collatz(num, pastNum)
    if moveCount > count:
        count = moveCount
        wanted = num

print(count)
print(wanted)
