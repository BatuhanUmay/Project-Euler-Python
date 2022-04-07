def compute():
    ans = sum(i
              for i in range(1000000)
              if bin(i)[2:] == bin(i)[2:][::-1] and str(i) == str(i)[::-1]
              )
    return ans


print(compute())
