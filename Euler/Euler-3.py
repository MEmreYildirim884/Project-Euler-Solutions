number = 13195
prime_factors = [
    i for i in range(2, number+1)
    if number % i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))
]

print("max prime is =", max(prime_factors))