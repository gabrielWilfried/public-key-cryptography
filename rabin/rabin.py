import random

# Function to generate prime numbers using Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform Miller-Rabin primality test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        if is_prime(prime_candidate):
            return prime_candidate

def generate_key_pair(bit_length):
    p = generate_large_prime(bit_length // 2)
    q = generate_large_prime(bit_length // 2)
    n = p * q
    return (p, q), n

def encrypt(plaintext, n):
    return pow(plaintext, 2, n)

def decrypt(ciphertext, p, q):
    n = p * q
    sqrt_ciphertext_p = pow(ciphertext, (p + 1) // 4, p)
    sqrt_ciphertext_q = pow(ciphertext, (q + 1) // 4, q)
    y_p = pow(p, -1, q)
    y_q = pow(q, -1, p)
    x = (sqrt_ciphertext_p * q * y_q + sqrt_ciphertext_q * p * y_p) % n
    return x

if __name__ == "__main__":
    bit_length = 128  # Choose the bit length for the key
    public_key, n = generate_key_pair(bit_length)
    p, q = public_key

    plaintext = int(input("Enter the plaintext (integer): "))
    ciphertext = encrypt(plaintext, n)
    print("Ciphertext:", ciphertext)

    decrypted_plaintext = decrypt(ciphertext, p, q)
    print("Decrypted plaintext:", decrypted_plaintext)
