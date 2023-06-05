from pwn import *
import re


def solve():
    ff_string = b"f" * 32

    p = remote("prf.sdc.tf", 1337)
    
    doors = 50
    while doors > 0:
        p.recvuntil(b"Enter a number: ")
        p.sendline(b"3")
        p.sendline(b"0" * 32)

        left_door = p.recvline().decode("utf-8")
        test_hex = re.findall("[0-9a-f]{64}", left_door)[0]
        ff_part = test_hex[32:]

        p.recvuntil(b"Enter a number: ")
        p.sendline(b"3")
        p.sendline(ff_part.encode())

        result = p.recvline().decode("utf-8")
        result_hex = re.findall("[0-9a-f]{64}", result)[0]

        p.recvuntil(b"Enter a number: ")

        if ff_string.decode("utf-8") in result_hex:
            p.sendline(b"2")
        else:
            p.sendline(b"1")

        doors -= 1

    for _ in range(5):
        print(p.recvline())


if __name__ == "__main__":
    solve()

# sdctf{n07_V3rY_pS3uD0R4nD0m_a6d137}