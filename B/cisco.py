from string import ascii_lowercase

s = input()
n = len(s)
consonants = [c for c in ascii_lowercase if c not in 'aeiou']

count = ['NO' for _ in range(n+1)]
for x in consonants:
    for y in consonants:
        if x != y:
            length = n - s.count(x + y)
            if count[length] == 'NO':
                count[length] = x + y

print(*count[1:])
