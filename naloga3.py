n = int(input())

prastevila = [True] * (n+1)
i = 2
while i**2 <= n:
    if prastevila[i]:
        for j in range(2*i, n+1, i):
            prastevila[j] = False
    i += 1
prastevila = [i for i, x in enumerate(prastevila) if x and i > 1]

prafaktorji = []
while n > 1:
    for i in prastevila:
        if n%i == 0:
            prafaktorji.append(i)
            n /= i
            break

# print('*'.join(prafaktorji))

from collections import defaultdict
prafaktorji2 = defaultdict(lambda: 0)
for p in prafaktorji:
    prafaktorji2[p] += 1
print('*'.join([(f'{k}^{v}' if v > 1 else f'{k}') for k, v in prafaktorji2.items()]))
