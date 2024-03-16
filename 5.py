f = open("products.csv", encoding="UTF-8").read().split("\n") #чтение файла
f.pop(0)
a = []
for i in f: #добовляю в массив a все котикории и их сумму продаж
    b = i.split(';')
    p = -1
    for j in range(len(a)):
        if a[j][1] == b[0]:
            p = j
    if p == -1:
        a.append([float(b[4]), b[0]])
    else:
        a[p][0] += float(b[4])
a.sort()
for i in range(0, 10): #вывод
    print(a[i][1], a[i][0])