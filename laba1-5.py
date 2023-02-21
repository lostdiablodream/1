N = int(input('Введите N: '))
a = ''
for i in range(N):
    str = input('Введите слово: ')
    a = (a + (str + ' '))
print(a)