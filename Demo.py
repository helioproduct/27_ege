file = open('source/1/27.txt', 'r')


def get():
    string = file.readline()
    if string.count(' ') == 0:
        return int(string)
    reg_ex = ' ' * string.count(' ')
    return list(map(int, string.split(reg_ex)))


n = get()

'''
Изначально содержит первую пару,
далее принимает значение максимальной суммы с остатками 
от деления на 3 (0, 1, 2)
'''

s = get()

for _ in range(n - 1):
    pair = get()
    # Берем число из первой (s) и второй пары (pair)
    sums = [i+j for i in s for j in pair]

    filtered = [0] * 3
    for x in sums:
        filtered[x % 3] = max(x, filtered[x % 3])
    s = [x for x in filtered if x != 0]

    # print('Всевозможные суммы:', sums)
    # print('Выбранные суммы:', s)


print('ANSWER:', max(s[1:]))