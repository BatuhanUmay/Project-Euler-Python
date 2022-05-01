def summation_of_cubes(n):
    ans = sum(i ** i
              for i in range(n, 0, -1))
    return str(ans)


print(summation_of_cubes(1000)[-10:])

##################################################################

# def compute():
#     MOD = 10 ** 10
#     ans = sum(pow(i, i, MOD) for i in range(1, 1001)) % MOD
#     return str(ans)
#
#
# if __name__ == "__main__":
#     print(compute())
