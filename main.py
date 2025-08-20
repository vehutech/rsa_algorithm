import random
import math
from validatePrime import isPrime
from genPrime import generatePrime
from modeInverse import modInverse
from userInput import userInput

def main():
    print("WELCOME")
    print("A CLI APPLICATION SHOWCASING RSA ENCRYPTION TECHNIQUE")
    print("RSA is an encryption technique used as a security layer between people, having a public and a private key.")
    
    try:
        minVal = userInput("minimum")
        maxVal = userInput("maximum")
        
        # Validation
        if minVal >= maxVal:
            print("Error: minimum value must be less than maximum value.")
            return
        
        # For RSA to work properly, we need reasonably large primes
        if maxVal < 10:
            print("Warning: Very small numbers may not work well with RSA encryption.")
            print("Consider using larger numbers (at least 100) for better results.")
        
        print(f"Min Value = {minVal}")
        print(f"Max Value = {maxVal}")
        
        # Generate two different primes
        p = generatePrime(minVal, maxVal)
        q = generatePrime(minVal, maxVal)
        
        # Ensure p and q are different
        attempts = 0
        while p == q and attempts < 10:
            q = generatePrime(minVal, maxVal)
            attempts += 1
        
        if p == q:
            print("Warning: Could not generate two different primes. Results may not be secure.")
        
        n = p * q
        phi_of_n = (p - 1) * (q - 1)
        
        # Choose e such that 1 < e < phi_of_n and gcd(e, phi_of_n) = 1
        e = 3  # Start with a small odd number
        while e < phi_of_n:
            if math.gcd(e, phi_of_n) == 1:
                break
            e += 2  # Only check odd numbers
        
        if e >= phi_of_n:
            print("Error: Could not find suitable public key exponent")
            return
        
        try:
            d = modInverse(e, phi_of_n)
        except ValueError as ve:
            print(f"Error calculating private key: {ve}")
            return
        
        publicKey = e
        privateKey = d
        
        print(f"Public Key: {publicKey}")
        print(f"Private Key: {privateKey}")
        print(f"n: {n}")
        print(f"Phi of N: {phi_of_n}")
        print(f"Prime Number 1: {p}")
        print(f"Prime Number 2: {q}")
        
        # Test encryption/decryption
        message = "Hello World"
        print(f"\nOriginal message: {message}")
        
        # Check if message characters can be encrypted (ord(c) < n)
        max_char_value = max(ord(c) for c in message)
        if max_char_value >= n:
            print(f"Error: Message contains characters that cannot be encrypted.")
            print(f"Maximum character value: {max_char_value}, but n = {n}")
            print("Try using larger prime numbers.")
            return
        
        # Encryption
        message_encoded = [ord(c) for c in message]
        print(f"Message as ASCII: {message_encoded}")
        
        cipherText = [pow(c, e, n) for c in message_encoded]
        print(f"Encrypted: {cipherText}")
        
        # Decryption
        decrypted_encoded = [pow(ch, d, n) for ch in cipherText]
        decrypted_message = "".join(chr(ch) for ch in decrypted_encoded)
        print(f"Decrypted: {decrypted_message}")
        
        # Verify decryption worked
        if message == decrypted_message:
            print("✓ Encryption/Decryption successful!")
        else:
            print("✗ Encryption/Decryption failed!")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()