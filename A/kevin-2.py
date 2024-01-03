from itertools import product, count
 
def good(*s):
    return {*'ABC'} in map(set, zip(*(s[i:] for i in range(3))))
 
def solve(n, s):
    return next(l for l in count() if any(good(*s, *t) for t in product('ABC', repeat=l)))
 
if __name__ == '__main__':
    print(solve(int(input()), input()))
