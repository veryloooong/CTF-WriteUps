# Modulo as a Service

Cryptography, 410pts

> Welcome to MaaS - Modulo as a Service! `nc challs.n00bzunit3d.xyz 51081`

## Analysis

Looking at the source code, I see a few peculiar items:

* The hidden text is all capital letters and is 16 characters long.
* For each letter, you get 3 chances to guess the letter, by inputting a number and the program returning `number << 16 % ord(c)`.

Which means, given 3 guesses, we need to generate a trio of values with can uniquely identify any letter from A to Z, or ASCII values 65 to 90.

## Solution

I just randomly chose numbers that are somewhat distant enough from one another, such as it surpasses the modulus and generate slightly different values. My chosen inputs were 1, 5, and 10.

Then for each number, I generated an array `arr = [num << 16 % 65, num << 16 % 66, ...]`. Then I confirmed the values at each index created a unique trio, and then created a simple hash by concatenating them.

Then it was just a matter of automating the checks. The script is in a separate file on my GitHub, but you can also view it here.

```python
from pwn import *

p = remote("challs.n00bzunit3d.xyz", 51081)

arr1 = [16, 64, 10, 52, 55, 16,  3, 16, 55, 46, 61, 24,  9, 16, 45, 16,  7, 18, 49, 16,  1,  4, 25, 64, 32, 16]
arr2 = [15, 56, 50, 56, 68, 10, 15,  8, 56,  8,  5, 44, 45,  2, 67,  0, 35,  8, 79, 80,  5, 20, 38, 56, 71, 80]
arr3 = [30, 46, 33, 44, 67, 20, 30, 16, 39, 16, 10, 12, 13,  4, 55,  0, 70, 16, 75, 76, 10, 40, 76, 24, 53, 70]

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
```

After running, we receive the flag.

`n00bz{M0dul0_f7w_1a4d3f5c!}`