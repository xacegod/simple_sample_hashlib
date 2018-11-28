import hashlib

v0 = b"filip"
m0 = hashlib.sha256()
m0.update(v0)
h0 = m0.digest()

i = 0

while True:
    # nonce hash
    nonce = str(i).encode()
    m1 = hashlib.sha256()
    m1.update(nonce)
    h1 = m1.digest()

    # final hash
    m2 = hashlib.sha256()
    m2.update(h0)
    m2.update(h1)
    h = m2.digest()

    if h.startswith(b'000'):
        break

    i += 1

print(f'h0: {h0!r}')
print(f'h1: {h1!r}')
print(f'h: {h!r}')
print(f'nonce: {nonce!r}')
