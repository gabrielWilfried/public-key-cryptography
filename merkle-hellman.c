#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Generate a superincreasing knapsack
void generate_superincreasing_knapsack(int n, int *q, int *w) {
    srand(time(NULL));
    *q = rand() % (2 * n - (n + 1)) + (n + 1);
    for (int i = 0; i < n; i++) {
        w[i] = rand() % (*q - 1) + 1;
    }
}

// Generate a private and public key pair
void generate_key_pair(int n, int *q, int *w, int *r, int *beta) {
    generate_superincreasing_knapsack(n, q, w);
    *r = rand() % (*q - 2) + 2;
    for (int i = 0; i < n; i++) {
        beta[i] = (*r * w[i]) % (*q);
    }
}

// Encrypt a message using the public key
int encrypt(int *message, int *beta, int n) {
    int ciphertext = 0;
    for (int i = 0; i < n; i++) {
        ciphertext += message[i] * beta[i];
    }
    return ciphertext;
}

// Decrypt a ciphertext using the private key
void decrypt(int ciphertext, int *w, int *s, int n) {
    for (int i = n - 1; i >= 0; i--) {
        if (ciphertext >= w[i]) {
            s[i] = 1;
            ciphertext -= w[i];
        } else {
            s[i] = 0;
        }
    }
}

// Pad the message to match the length of the public key
void pad_message(int *message, int *w, int *padded_message, int n) {
    int message_len = sizeof(message) / sizeof(int);
    if (message_len < n) {
        for (int i = 0; i < n - message_len; i++) {
            padded_message[i] = 0;
        }
        for (int i = n - message_len; i < n; i++) {
            padded_message[i] = message[i - (n - message_len)];
        }
    } else if (message_len > n) {
        // Throw an error or handle the case where message length exceeds knapsack length
    } else {
        for (int i = 0; i < n; i++) {
            padded_message[i] = message[i];
        }
    }
}

// Unpad the decrypted message
void unpad_message(int *padded_message, char *unpadded_message, int n) {
    for (int i = 0; i < n; i++) {
        unpadded_message[i] = (char)(padded_message[i] + '0');
    }
    unpadded_message[n] = '\0';
}

int main() {
    int n = 64;  // Adjust n for desired security level
    int q, w[n], r, beta[n];
    int public_key[2], private_key[2];
    generate_key_pair(n, &q, w, &r, beta);
    public_key[0] = q;
    for (int i = 0; i < n; i++) {
        public_key[1][i] = beta[i];
    }
    private_key[0] = q;
    for (int i = 0; i < n; i++) {
        private_key[1][i] = w[i];
    }

    printf("Private key (q, w): (%d, [", q);
    for (int i = 0; i < n; i++) {
        printf("%d", w[i]);
        if (i != n - 1) {
            printf(", ");
        }
    }
    printf("])\n");

    printf("Public key (q, beta): (%d, [", q);
    for (int i = 0; i < n; i++) {
        printf("%d", beta[i]);
        if (i != n - 1) {
            printf(", ");
        }
    }
    printf("])\n");

    int message[] = {0, 1, 0, 1, 1, 0, 1, 0};  // Binary message
    int padded_message[n];
    pad_message(message, w, padded_message, n);
    int ciphertext = encrypt(padded_message, beta, n);
    printf("Ciphertext: %d\n", ciphertext);

    char unpadded_message[n];
    decrypt(ciphertext, w, unpadded_message, n);
    printf("Decrypted message: %s\n", unpadded_message);

    return 0;
}
