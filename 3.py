def sooor_str(b, p): #сортировка вставками для строк(string)
    for i in range(1, len(b)):
        x = b[i]
        j = i
        while j > 0 and (b[j - 1][p]) > (x[p]):
            b[j] = b[j - 1]
            j -= 1
        b[j] = x
    return b

def sooor_float(b, p): #сортировка вставками для дроби(float)
    for i in range(1, len(b)):
        x = b[i]
        j = i
        while j > 0 and float(b[j - 1][p]) > float(x[p]):
            b[j] = b[j - 1]
            j -= 1
        b[j] = x
    return b

f = open("products.csv", encoding="UTF-8").read().split('\n')#чтение файла
f.pop(0)
a = []
for i in f:
    a.append(i.split(';'))
a = sooor_float(a, 4)
a = sooor_str(a, 0)#сортирую
print(a)
while(1):#основной цикол программы
    b = str(input())# принемаю данные от пользователя
    if b == "молоко":#остоновка вслучие ввода контрольного слова "молоко"
        break
    p = -1
    for i in range(len(a)): #нахожу самый дороггой товар в первой котигории
        if a[i][0] != b:
            p = i - 1
            break
    if p == -1:#вывод в консоль
        print("Такой категории не существует в нашей БД")
    else:
        print("В категории:", a[p][0], "товар:", a[p][1], "был куплен", a[p][4], "раз")