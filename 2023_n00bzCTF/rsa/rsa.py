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

# n00bz{5m4ll_3_1s_n3v3r_g00d!}