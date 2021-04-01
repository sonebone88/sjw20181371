from math import gcd

p = 13
q = 17
n = p * q
phi_n = (p-1) * (q-1)

# e = gcd(phi_n, e) = 1, 1<e<phi_n
# or use Euclidean algorithm
e = 0
while True:
    e += 1
    if gcd(phi_n,e) == 1:
        break

d = 0
mod = 0
while True:
    d += 1
    mod = (e * d) % phi_n
    if mod == 1:
        break

# Encryption
# C = P^e mod n

plain = "any plain text"
plain_list = [ord(x) for x in plain]

cipher = []
for i in plain_list:
    x = (i ** e) % n
    cipher.append(int(x))

# Decryption
# P = C^d mod n

decrypted = []
for i in cipher:
    x = (i ** d) % n
    decrypted.append(int(x))

print('plain text', plain_list)
print('cipher text', cipher)
print('decrypted text', decrypted)

print([chr(x) for x in decrypted])
decrypted_text = ''.join([chr(x) for x in decrypted])
print(decrypted_text)
