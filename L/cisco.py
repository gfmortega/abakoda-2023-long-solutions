consonants = set('QWRTYPSDFGHJKLZXCVBNM')

s = ''.join(c for c in input().upper() if c in consonants)
k = int(input())
n = len(s)

if k > 2**(n-1):
    print('out of bounds')
else:
    def binary(v, bit_count):
        ans = []
        for _ in range(bit_count):
            ans.append(v & 1)
            v >>= 1
        return reversed(ans)

    ans = [s[0]]
    for bit, c in zip(binary(k-1, n-1), s[1:]):
        if bit == 0:
            ans.append(' ')
        ans.append(c)
    
    print(''.join(ans))
