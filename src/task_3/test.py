from Crypto.Util.number import isPrime, long_to_bytes, inverse
from math import isqrt
import binascii

# Дано:
n = 55089599753625499150129246679078411260946554356961748980861372828434789664694269460953507615455541204658984798121874916511031276020889949113155608279765385693784204971246654484161179832345357692487854383961212865469152326807704510472371156179457167612793412416133943976901478047318514990960333355366785001217
e = 65537

def fermat_factor(n):
    a = isqrt(n)
    if a * a < n:
        a += 1
    b2 = a * a - n
    while not isqrt(b2) ** 2 == b2:
        a += 1
        b2 = a * a - n
    b = isqrt(b2)
    return a - b, a + b

p, q = fermat_factor(n)
print(f"p = {p}\nq = {q}")


phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(f"d = {d}")


with open("ciphertext.txt", "r") as f:
    ciphertext_hex = f.read().strip()

ciphertext = int(ciphertext_hex, 16)
m = pow(ciphertext, d, n)

flag = long_to_bytes(m)
print(flag)
