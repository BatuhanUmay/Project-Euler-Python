def compute(num):

    sumPrime = []

    for j in range(2, num + 1):
        prime = True
        for i in range(2, int(pow(j, 0.5)) + 1):
            if j % i == 0:
                prime = False
                break

        if prime:
            sumPrime.append(j)

    print(sum(sumPrime))

compute(2000000)

#############################################################################

# import eulerlib
#
#
# # Call the sieve of Eratosthenes and sum the primes found.
# def compute():
# 	ans = sum(eulerlib.list_primes(1999999))
# 	return str(ans)
#
#
# if __name__ == "__main__":
# 	print(compute())