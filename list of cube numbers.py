#wap to print list of prime numbers.
prime_numbers=[]
start = 2  # Starting from 2, the first prime number
end = 100  # Up to 100

# Loop through the range
for num in range(start, end + 1):
    is_prime = True  # Assume the number is prime
    if num > 1:  # Check only for numbers greater than 1
        for i in range(2, int(num**0.5) + 1):  # Check divisibility
            if num % i == 0:  # If divisible, it's not prime
                is_prime = False
                break  # Exit the inner loop
        if is_prime:  # If it remains prime, append to the list
            prime_numbers.append(num)

# Print the list of prime numbers
print(prime_numbers)
