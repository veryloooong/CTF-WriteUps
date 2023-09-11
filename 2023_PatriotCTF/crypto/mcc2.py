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
