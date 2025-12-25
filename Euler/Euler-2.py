

fib_numbers = [0, 1]
while True:
    next_fib = fib_numbers[-1] + fib_numbers[-2]
    if next_fib > 1000:
        break
    fib_numbers.append(next_fib)

print("even fibonnaci numbers are :")
sum=0
for i in fib_numbers:
    if i%2==0:
        sum+=i
        print(i)
print("the sum is : ", sum)









