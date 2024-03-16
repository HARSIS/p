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
a = sooor_float(a, 3)
a = sooor_str(a, 0)
b = a[0][0]
p = -1
for i in range(len(a)): #нахожу самый дороггой товар в первой котигории
    if a[i][0] != b:
        p = i - 1
        break
print("В категории:", a[p][0], "самый дорогой товар:", a[p][1], "его цена за единицу товара составляет", a[p][3]) #вывод в консоль