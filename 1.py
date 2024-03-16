f = open("products.csv", encoding="UTF-8").read().split("\n") #чтение файла
f[0] = f[0] + ";total"
for i in range(1, len(f)):
    a = f[i].split(';')
    f[i] = f[i] + ";" + str(float(a[3]) * float(a[4])) #добовление столбца
f = "\n".join(f)
open("products_new.csv", mode="w", encoding="UTF-8").write(f) # запись файла
