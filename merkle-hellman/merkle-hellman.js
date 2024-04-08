// Function to generate a superincreasing knapsack
function generateSuperincreasingKnapsack(n) {
    let q = Math.floor(Math.random() * (2 * n - (n + 1) + 1)) + (n + 1);
    let w = [];
    for (let i = 0; i < n; i++) {
        w.push(Math.floor(Math.random() * (q - 1)) + 1);
    }
    return { q: q, w: w };
}

// Function to generate a private and public key pair
function generateKeyPair(n) {
    let { q, w } = generateSuperincreasingKnapsack(n);
    let r = Math.floor(Math.random() * (q - 2)) + 2;
    let beta = w.map((wi) => (r * wi) % q);
    return { privateKey: { q: q, w: w }, publicKey: { q: q, beta: beta } };
}

// Function to encrypt a message using the public key
function encrypt(message, publicKey) {
    let { q, beta } = publicKey;
    let ciphertext = 0;
    for (let i = 0; i < message.length; i++) {
        ciphertext += message[i] * beta[i];
    }
    return ciphertext;
}

// Function to decrypt a ciphertext using the private key
function decrypt(ciphertext, privateKey) {
    let { q, w } = privateKey;
    let s = new Array(w.length).fill(0);
    for (let i = w.length - 1; i >= 0; i--) {
        if (ciphertext >= w[i]) {
            s[i] = 1;
            ciphertext -= w[i];
        }
    }
    return s;
}

// Function to pad the message to match the length of the public key
function padMessage(message, publicKey) {
    let n = publicKey.beta.length;
    let messageLen = message.length;
    if (messageLen < n) {
        let padding = new Array(n - messageLen).fill(0);
        return padding.concat(message);
    } else if (messageLen > n) {
        throw new Error("Message length exceeds knapsack length");
    } else {
        return message;
    }
}

// Function to unpad the decrypted message
function unpadMessage(paddedMessage) {
    return paddedMessage.map(String);
}

// Example usage
let { publicKey, privateKey } = generateKeyPair(64);
console.log("Private key (q, w):", privateKey);
console.log("Public key (q, beta):", publicKey);

let message = [0, 1, 0, 1, 1, 0, 1, 0]; // Binary message
let paddedMessage = padMessage(message, publicKey);
let ciphertext = encrypt(paddedMessage, publicKey);
console.log("Ciphertext:", ciphertext);

let decryptedMessage = decrypt(ciphertext, privateKey);
let unpaddedMessage = unpadMessage(decryptedMessage);
console.log("Decrypted message:", unpaddedMessage);
