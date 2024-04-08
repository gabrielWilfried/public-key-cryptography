'''
    This code implements the Merkle-Hellman knapsack cryptosystem, which is a public-key cryptosystem based on the subset sum problem. Here's a breakdown of the code:

1. Generating Superincreasing Knapsack:
   - The `generate_superincreasing_knapsack` function generates a superincreasing knapsack, which is a sequence of positive integers where each element is greater than the sum of all the preceding elements.
   - It randomly generates a modulus `q` between `n + 1` and `2 * n`, where `n` is the length of the knapsack.
   - It generates `n` random integers `w[i]` between `1` and `q - 1` to form the knapsack weights.

2. Generating Key Pair:
   - The `generate_key_pair` function generates a private and public key pair.
   - It first generates a superincreasing knapsack using `generate_superincreasing_knapsack`.
   - It then generates a random integer `r` between `2` and `q - 1`, where `q` is the modulus.
   - It calculates the public key `beta` as a list of integers by multiplying each knapsack weight `w[i]` with `r` modulo `q`.
   - It returns the private key as a tuple `(q, w)` and the public key as a tuple `(q, beta)`.

3. Encrypting a Message:
   - The `encrypt` function takes a binary message and encrypts it using the public key.
   - It unpacks the public key tuple `(q, beta)`.
   - It calculates the ciphertext by summing the products of each message bit and its corresponding beta value.

4. Decrypting a Ciphertext:
   - The `decrypt` function decrypts a ciphertext using the private key.
   - It unpacks the private key tuple `(q, w)`.
   - It iterates through the knapsack weights in reverse order and updates the decrypted message bits based on whether the current weight can be subtracted from the ciphertext.

5. Padding and Unpadding Messages:
   - The `pad_message` function pads a message with zeros to match the length of the public key.
   - The `unpad_message` function converts the decrypted message from a list of bits to a list of strings.

6. Example Usage:
   - The example usage section generates a key pair, encrypts a binary message, decrypts the ciphertext, and prints the results.

This code demonstrates the basic implementation of the Merkle-Hellman knapsack cryptosystem. However, it's worth noting that this cryptosystem is vulnerable to certain attacks and is not typically used in practice due to its lack of security.
'''
# import random

# # Generate a superincreasing knapsack
# def generate_superincreasing_knapsack(n):
#     q = random.randint(n + 1, 2 * n)
#     w = [random.randint(1, q - 1) for _ in range(n)]
#     return q, w

# # Generate a private and public key pair
# def generate_key_pair(n):
#     q, w = generate_superincreasing_knapsack(n)
#     r = random.randint(2, q - 1)
#     beta = [(r * wi) % q for wi in w]
#     return (q, w), (q, beta)  # Return private key as tuple (q, w) and public key as tuple (q, beta)



# # Encrypt a message using the public key
# def encrypt(message, public_key):
#     q, beta = public_key  # Unpack the public key tuple
#     return sum(message[i] * beta[i] for i in range(len(message)))


# # Decrypt a ciphertext using the private key
# def decrypt(ciphertext, private_key):
#     q, w = private_key
#     s = [0] * len(w)
#     for i in range(len(w) - 1, -1, -1):
#         if ciphertext >= w[i]:
#             s[i] = 1
#             ciphertext -= w[i]
#     return s

# # Pad the message to match the length of the public key
# def pad_message(message, public_key):
#     if not isinstance(public_key[1], list):
#         raise ValueError("Knapsack weights should be provided as a list")
    
#     n = len(public_key[1])
#     message_len = len(message)
    
#     if message_len < n:
#         padding = [0] * (n - message_len)
#         return padding + message
#     elif message_len > n:
#         raise ValueError("Message length exceeds knapsack length")
#     else:
#         return message


# # Unpad the decrypted message
# def unpad_message(padded_message):
#     return [str(bit) for bit in padded_message]


# # Example usage
# if __name__ == "__main__":
#      # Generate a key pair
#     public_key, private_key = generate_key_pair(64)  # Adjust n for desired security level
#     q, w = private_key  # Unpack private key tuple
#     print("Private key (q, w):", private_key)
#     print("Public key (q, beta):", (q, public_key))

#     # Encrypt a message
#     message = [0, 1, 0, 1, 1, 0, 1, 0]  # Binary message
#     padded_message = pad_message(message, public_key)
#     ciphertext = encrypt(padded_message, public_key)
#     print("Ciphertext:", ciphertext)

#     # Decrypt the ciphertext
#     decrypted_message = decrypt(ciphertext, private_key)
#     unpadded_message = unpad_message(decrypted_message)
#     print("Decrypted message:", unpadded_message)



    # In this version, the output is converted in hexadecimal format

import random

# Generate a superincreasing knapsack
def generate_superincreasing_knapsack(n):
    q = random.randint(n + 1, 2 * n)
    w = [random.randint(1, q - 1) for _ in range(n)]
    return q, w

# Generate a private and public key pair
def generate_key_pair(n):
    q, w = generate_superincreasing_knapsack(n)
    r = random.randint(2, q - 1)
    beta = [(r * wi) % q for wi in w]
    return (q, w), (q, beta)  # Return private key as tuple (q, w) and public key as tuple (q, beta)

# Encrypt a message using the public key
def encrypt(message, public_key):
    q, beta = public_key  # Unpack the public key tuple
    return sum(message[i] * beta[i] for i in range(len(message)))

# Decrypt a ciphertext using the private key
def decrypt(ciphertext, private_key):
    q, w = private_key
    s = [0] * len(w)
    for i in range(len(w) - 1, -1, -1):
        if ciphertext >= w[i]:
            s[i] = 1
            ciphertext -= w[i]
    return s

# Pad the message to match the length of the public key
def pad_message(message, public_key):
    if not isinstance(public_key[1], list):
        raise ValueError("Knapsack weights should be provided as a list")
    
    n = len(public_key[1])
    message_len = len(message)
    
    if message_len < n:
        padding = [0] * (n - message_len)
        return padding + message
    elif message_len > n:
        raise ValueError("Message length exceeds knapsack length")
    else:
        return message

# Unpad the decrypted message
def unpad_message(padded_message):
    hex_message = ''.join(str(bit) for bit in padded_message)
    return hex(int(hex_message, 2))[2:]  # Convert binary to hexadecimal and remove '0x' prefix

# Example usage
if __name__ == "__main__":
     # Generate a key pair
    public_key, private_key = generate_key_pair(64)  # Adjust n for desired security level
    q, w = private_key  # Unpack private key tuple
    print("Private key (q, w):", private_key)
    print("Public key (q, beta):", (q, public_key))

    # Encrypt a message
    message = [0, 1, 0, 1, 1, 0, 1, 0]  # Binary message
    padded_message = pad_message(message, public_key)
    ciphertext = encrypt(padded_message, public_key)
    print("Ciphertext:", ciphertext)

    # Decrypt the ciphertext
    decrypted_message = decrypt(ciphertext, private_key)
    unpadded_message = unpad_message(decrypted_message)
    print("Decrypted message (hexadecimal):", unpadded_message)


