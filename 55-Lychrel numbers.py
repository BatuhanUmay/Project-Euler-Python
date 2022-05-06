def is_palindrome(num):
    return True if num == int(str(num)[::-1]) else False


def is_lychrel_number(num):
    for recursive in range(50):
        num += int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True


def compute():
    ans = sum(1
              for i in range(10000)
              if is_lychrel_number(i))
    return ans


if __name__ == "__main__":
    print(compute())
