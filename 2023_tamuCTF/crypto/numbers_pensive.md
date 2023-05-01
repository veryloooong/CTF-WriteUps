# Numbers :pensive:

Cryptography, 500- pts

> It wouldn't be a real CTF without some contrived RSA challenge, right?

We are given the public key `n`, a common `e = 65537`, and we are prompted to enter another value `e'` which will be used to generate a `d'`. There are a few ways to tackle this, but I used *mathematics* (lol) to solve this challenge.

> TLDR: A simpler solution is to enter `e'` as `-1`. Since `-1 mod phi = phi - 1`, you have calculated `phi`, `e` and `n`, which is adequate to encode/decode any message.

The way I solved it is thanks to [an algorithm](https://www.di-mgt.com.au/rsa_factorize_n.html) to calculate primes `p` and `q`, given `d` and `e`. I plan to use `p` and `q` to construct the RSA encryption from the ground up. The script did not take long to write, but the solution certainly could have been much faster.

```python
from Crypto.Random.random import randint
from math import gcd
from sys import exit

e = int(input("Enter e: ")) # Since the challenge allows the user to choose e, preferably enter a small e
d = int(input("Enter d: "))
n = int(input("Enter n: "))

k = d * e - 1

while True:
    t = k
    g = randint(2, n - 1)

    while t % 2 == 0:
        try:
            t = t // 2
        except OverflowError:
            print("Use a smaller e")
            exit(1)
        x = pow(g, t, n)
        if x > 1:
            y = gcd(x - 1, n)
            if y > 1:
                q = y
                print(f"q = {q}")
                exit(0)
```

After finding prime `q` you can easily calculate every other value and decode `c`, using online tools like [dCode](https://www.dcode.fr/rsa-cipher).

`gigem{h4h4_numb3rs_ar3_s0_qu1rky}`