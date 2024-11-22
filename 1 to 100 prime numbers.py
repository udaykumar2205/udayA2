#wap to print list of fibonacci numbers.
limit = 100
fibonacci_numbers = [0, 1]
for _ in range(2, limit):                       # Start from the 3rd position
    next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Calculate the next Fibonacci number
    if next_fib > limit:                        # Break if the next number exceeds the limit
        break
    fibonacci_numbers.append(next_fib)          # Append the next Fibonacci number to the list


print(fibonacci_numbers)
