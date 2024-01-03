n = int(input())
s = input()
if any(len(set(s[i:i+3])) == 3 for i in range(n-2)):
    print(0)
elif n > 1 and s[-2] != s[-1]:
    print(1)
else:
    print(2)
