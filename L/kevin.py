s = ''.join(ch for ch in input().upper() if ch.lower() != ch not in {*'AEIOU'})
t = '1' + bin(int(input()) - 1).lstrip('0b').rjust(len(s) - 1, '0')
print(''.join(' '*(tt == '0') + ss for ss, tt in zip(s, t)) if len(s) == len(t) else 'out of bounds')
