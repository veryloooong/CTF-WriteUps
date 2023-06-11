# RSA

Cryptography, 452pts

> Good old RSA! `nc challs.n00bzunit3d.xyz 2069`

## Analysis

The public exponent `e` is 17, which is kinda small. But `n` is especially large, which means FactorDB or common attacks are not going to be useful. However, when `nc`ing again, I see a different `n`. This means I can generate a set of `c`s and `n`s, and assuming they are just sending the same message encrypted differently, I can use **Hastad's broadcast attack**. 

## Explanation?

Since $m^e \equiv c\ (\textrm{mod}\ n)$, and $n$ is a product of two primes, it is highly likely that when I `nc` twice, the two $n$ values are going to be different. This means we can find $m^e$ with the **Chinese Remainder Theorem**.

The CRT states that given a set of pairwise coprime moduli $(m_1, m_2, \ldots, m_n)$, the equation system

$$
x \equiv a_1\ (\textrm{mod}\ m_1) \\
\ldots \\
x \equiv a_n\ (\textrm{mod}\ m_n) \\
$$

has a unique solution $x\ \textrm{mod}\ M$ with $M = \prod m_i$.

With 17 equations, we can find $m^{17}$ and then just take the 17th root to find $m$.

Of course, we also need a few checks to ensure we are not getting a different message modularly congruent to our message. This is where we are going to properly implement our algorithm.

> Read more: [Broadcast Attack](https://en.wikipedia.org/wiki/Coppersmith's_attack#Håstad's_broadcast_attack)

## The Game Plan

We implement the CRT solver first. Then we implement the Hastad's attack as an expansion of the CRT solver. This is actually already done before for us: check out [this repo](https://github.com/ashutosh1206/Crypton.git).

Then we connect to our server 17 times to get 17 values for `c` and `n`, populate 2 arrays with the values, and put them into our solver. 

The script is in a separate file on my GitHub, and down below.

```python
from Crypto.Util.number import GCD, bytes_to_long, long_to_bytes
import gmpy2
from pwn import *
import re

# CRT for e = 17, then m ** 17 = c (mod n)
def crt(list_c, list_n):
    M = 1
    for i in list_n:
        M *= i
    list_b = [M // i for i in list_n]
    try:
        list_b_inv = [int(gmpy2.invert(list_b[i], list_n[i])) for i in range(len(list_n))]
    except:
        print('failed lol')
        return -1
    x = 0
    for i in range(len(list_n)):
        x += list_c[i] * list_b[i] * list_b_inv[i]
    return x % M

def hastad(cts, mods, e):
    m_exp = crt(cts, mods)
    if m_exp != 1:
        eth_root = gmpy2.iroot(m_exp, e)
        if eth_root[1]:
            return long_to_bytes(eth_root[0])
        else:
            return 'lol'
    else:
        return 'lol'

if __name__ == '__main__':
    cts = []
    mods = []

    for _ in range(17):
        p = remote('challs.n00bzunit3d.xyz', 2069)
        p.recvline()
        ct = p.recvline().decode()
        mod = p.recvline().decode()

        ct = re.findall(r'\d+', ct)[0]
        mod = re.findall(r'\d+', mod)[0]

        cts.append(int(ct))
        mods.append(int(mod))

    print(hastad(cts, mods, 17))
```

When the script finishes running, we obtain the flag.

`n00bz{5m4ll_3_1s_n3v3r_g00d!}`