def compute():
    perimeter = 1000

    for a in range(1, perimeter + 1):
        for b in range(a + 1, perimeter + 1):
            c = perimeter - (a + b)
            if c ** 2 == a ** 2 + b ** 2:
                return a * b * c


if __name__ == "__main__":
    print(compute())
