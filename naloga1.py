n = int(input())
m = int(input())

curr = 0
max_ = 0

for _ in range(m):
    n += int(input())

    if n >= 3200:
        curr += 1
    else:
        max_ = max(curr, max_)
        curr = 0

max_ = max(curr, max_)
print(max_)
