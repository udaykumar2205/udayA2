#wap to print 1 to 100 prime numbers.
n=int(input())
for num in range(2, 101):
    is_prime = True  # Assume the number is prime
    for i in range(2, int(num**0.5) + 1):  # Check divisibility
        if num % i == 0:  # If divisible, it's not prime
            is_prime = False
            break  # Exit the inner loop if not prime
    if is_prime:  # If still prime, print the number
        print(num)
