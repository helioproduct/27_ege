file = open('source/2/27-2b.txt')


def get():
    string = file.readline()
    reg_ex = ' ' * string.count(' ')
    return list(map(int, string.split(reg_ex)))


n = int(file.readline())
mn = -float('inf')
s = get()

# n - 1 - первую пару уже считали
for _ in range(n - 1):
    # получаем след. пару
    pair = get()

    # считаем всевозможные суммы из пред пар + след. пары
    temp = [i+j for i in s for j in pair]

    # список для распределения сумм по остатку на число (в данном случае 3)
    fake_s = [mn] * 3

    # меняем
    for x in temp:
        fake_s[x % 3] = max(fake_s[x % 3], x)

    s = [x for x in fake_s if x != mn]


print(s[0])