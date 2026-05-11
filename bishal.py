nums = [2,3,4,5,6,7]
primes = []

for i in nums:
    factors = []
    for j in range(i):
        if j ==0: continue
        if i%j  == 0:
            factors.append(j)
    if len(factors) == 1:
        primes.append(i)

print(primes)
