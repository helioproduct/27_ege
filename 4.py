# сумма делится на 5 и максимально возможная
file = open('source/4/27-4b.txt', 'r')


def get():
    return list(map(int, file.readline().split(' ')))


mn = -float('inf')
n = int(file.readline())
s = get()

for _ in range(n - 1):
    pair = get()
    sums = [a+b for a in s for b in pair]

    filtered = [mn] * 5
    for x in sums:
        filtered[x % 5] = max(x, filtered[x % 5])

    s = [sum for sum in filtered if sum != mn]


print(s[0])