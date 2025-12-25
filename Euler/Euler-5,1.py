# In first solution we found the number which contains that prime number most and we multiply each of them
import math

upper_limit = 20

# Finding primes up to 20 and calculating the maximum power for each
results = {p: int(math.log(upper_limit, p)) for p in range(2, upper_limit + 1) if all(p % i for i in range(2, int(p**0.5) + 1))}

print(results)

number = pow(2,4) * pow(3,2) * pow(5,1) * pow(7,1) * pow(11,1) * pow(13,1) * pow(17,1) * pow(19,1)
print(number)