a = []
n = -1

while n == -1 or n > 0:
    x = list(map(int, input().split()))

    a.append(x)
    n = len(x) - 1

def max_force(i, j): # i: trenuten layer, j: pozicija v tem layerju
    f = a[i][j]

    if i > 0:
        if a[i-1][j] > a[i-1][j+1]:
            f += max_force(i-1, j)
        elif a[i-1][j] < a[i-1][j+1]:
            f += max_force(i-1, j+1)
        else:
            f += max(max_force(i-1, j), max_force(i-1, j+1))

    return f

print(max_force(len(a)-1, 0))
