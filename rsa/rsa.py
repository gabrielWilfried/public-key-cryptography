import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num, k=5):
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    s, d = 0, num - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        x = pow(random.randint(2, num - 1), d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime(length=1024):
    p = generate_prime_candidate(length)
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def generate_key_pair(length=1024):
    p = generate_prime(length)
    q = generate_prime(length)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi - 1)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

if __name__ == "__main__":
    message = int(input("Enter the plaintext (integer): "))
    public_key, private_key = generate_key_pair()
    print("Public key (e, n):", public_key)
    print("Private key (d, n):", private_key)

    ciphertext = encrypt(message, public_key)
    print("Ciphertext:", ciphertext)

    decrypted_message = decrypt(ciphertext, private_key)
    print("Decrypted plaintext:", decrypted_message)
