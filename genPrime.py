import random
from validatePrime import isPrime

def generatePrime(minVal, maxVal):
    # Check if there are any primes in the range
    primes_in_range = [n for n in range(max(2, minVal), maxVal + 1) if isPrime(n)]
    if not primes_in_range:
        raise ValueError(f"No primes found in range {minVal} to {maxVal}")
    
    prime = random.randint(minVal, maxVal)
    attempts = 0
    max_attempts = 1000  # Prevent infinite loops
    
    while not isPrime(prime) and attempts < max_attempts:
        prime = random.randint(minVal, maxVal)
        attempts += 1
    
    if attempts >= max_attempts:
        # If random selection fails, pick from known primes
        return random.choice(primes_in_range)
    
    return prime
