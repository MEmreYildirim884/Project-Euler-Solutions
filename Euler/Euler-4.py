def solve_euler_4_optimized():
    max_palindrome = 0
    factors = (0, 0)
    
    #  Search from largest to smallest
    for a in range(999, 99, -1):
        
        #  (Early Exit): 
        # If a * a is smaller than our current record, no need to check further.
        if a * a <= max_palindrome:
            break
            
        #  (The Rule of 11):
        # At least one factor must be divisible by 11 to form a 6-digit palindrome.
        b_start = a
        step = 1
        
        if a % 11 != 0:
            b_start = a - (a % 11)
            step = 11
            
        for b in range(b_start, 99, -step):
            product = a * b
            
            if product <= max_palindrome:
                break
            
            # Palindrome check (We convert the number to a string because Python's slicing operator [::-1] provides a very fast and simple way)
            if str(product) == str(product)[::-1]:
                max_palindrome = product
                factors = (a, b)
                break 
                
    return max_palindrome, factors

result, numbers = solve_euler_4_optimized()
print(f"The largest palindrome is {result}, which is the product of {numbers[0]} and {numbers[1]}.")