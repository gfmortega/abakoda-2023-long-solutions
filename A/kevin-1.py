from itertools import product, count

def good(*s):
    return any(len({*s[i:i+3]}) == 3 for i in range(len(s)))

def solve(n, s):
    return next(l for l in count() if any(good(*s, *t) for t in product('ABC', repeat=l)))

if __name__ == '__main__':
    print(solve(int(input()), input()))
