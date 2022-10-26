def prime(n):
    is_prime = True
    if n == 1:
        return False
    else:
        for i in range(2, (int)(n // 2) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime

number = 600851475143
result = 1
primes = []
factors = []

for n in range(2, 1500):
  if prime(n):
    primes.append(n)

for x in primes:
  if number % x == 0:
    factors.append(x)

for x in factors:
  result *= x


print(number//result)

    