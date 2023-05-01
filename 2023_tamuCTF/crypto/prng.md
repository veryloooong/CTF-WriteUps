# PRNG

Cryptography, 500- pts

> I know they say don't roll your own crypto, but secure RNG should be easy. How hard could it be?

Looking at the source code we find that the `Rand` class essentially implements a [Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator).

```python
class Rand:
    def __init__(self, seed):
        self.m = m
        self.a = a
        self.c = c
        self.seed = seed
        if seed % 2 == 0: # initial state must be odd
            self.seed += 1

    def rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed
```

Since LCGs have been known to be cryptographically compromised, and are some of the most commonly seen PRNGs, there have been various tools to solve it. [This one](https://github.com/TomasGlgg/LCGHack) for example.

Entering the 10 values it gives us and asking for the next 10 values, we get the flag.

`gigem{D0nt_r0ll_y0uR_oWn_RnG}`