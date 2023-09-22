# Mason Competitive Cyber 2

Cryptography, 500- pts (Not solved during the competition)

> It seems that someone managed to break the encoding on our previous message and the secret got out! We've reinforced the secret encoding of our message so there's no way anyone can break it this time.

## Analysis

It appears this file also uses zero-width steganography by encoding letters with binary, but instead of `\u200C` and `\u200D`, it uses `\u2062` and `\u2063`. Using the knowledge from the first Mason Competitive Cyber challenge, I quickly decoded the message:

> You're halfway there, now use these numbers to solve the rest: 5 3 8 4 7 1

What?

## The solution

It appears that the numbers must be connected to the original message. That's when I see that there are 6 numbers, corresponding to the 6 characters in `MasonC`. So what else is there?

I removed all the invisible characters in the original file and downloaded it. One thing I tried was to perform a map from letters to numbers, and within each line use the numbers to do some operations. One of them I tried was to add the numbers on each row. And once the first line return the ASCII value for `P`, I know what I have to do.

The Python script is below.

```python
nums = {
    'M': 5,
    'a': 3,
    's': 8,
    'o': 4,
    'n': 7,
    'C': 1,
}

flag = ''

with open('./mason2.txt', 'r') as f:
    for row in f:
        row = row.rstrip()
        char = 0
        for c in row:
            char += nums[c]
        flag += chr(char)

print(flag)
```
