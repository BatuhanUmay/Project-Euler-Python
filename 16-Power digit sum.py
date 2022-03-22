res = str(pow(2, 1000))

# digits = 0
# for i in res:
#     digits += int(i)

digits = sum(int(i) for i in res)

print(digits)
