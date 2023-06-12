from pwn import *

p = remote("challs.n00bzunit3d.xyz", 51081)

arr1 = [16, 64, 10, 52, 55, 16,  3, 16, 55, 46, 61, 24,
        9, 16, 45, 16,  7, 18, 49, 16,  1,  4, 25, 64, 32, 16]
arr2 = [15, 56, 50, 56, 68, 10, 15,  8, 56,  8,  5, 44,
        45,  2, 67,  0, 35,  8, 79, 80,  5, 20, 38, 56, 71, 80]
arr3 = [30, 46, 33, 44, 67, 20, 30, 16, 39, 16, 10, 12,
        13,  4, 55,  0, 70, 16, 75, 76, 10, 40, 76, 24, 53, 70]


def hash(a, b, c):
    return a * 10000 + b * 100 + c


arr = list(map(hash, arr1, arr2, arr3))

print(arr)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

guess = ''

for _ in range(16):
    p.recvuntil(b'Enter Guess:')
    p.sendline(b'1')
    g1 = p.recvline().decode().strip()
    p.recvuntil(b'Enter Guess:')
    p.sendline(b'5')
    g2 = p.recvline().decode().strip()
    p.recvuntil(b'Enter Guess:')
    p.sendline(b'10')
    g3 = p.recvline().decode().strip()
    g1, g2, g3 = map(int, (g1, g2, g3))
    print(g1, g2, g3)

    i = arr.index(hash(g1, g2, g3))
    guess += alpha[i]

p.recvuntil(b'Enter Guess:')
p.sendline(guess.encode())
print(p.recvline())
