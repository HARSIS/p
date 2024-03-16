f = open("products.csv", encoding="UTF-8").read().split("\n") #чтение файла
f[0] = f[0] + ";promocode"
for i in range(1, len(f)): #добовляю столбец
    a = f[i].split(';')
    f[i] = f[i] + ";" + a[1][:2] + a[2][:2] + a[1][-1] + a[1][-2] + a[2][4] + a[2][3]#собираю строчку
    f[i] = f[i].upper()#делаю все буквы загалные
f = "\n".join(f)
open("product_promo.csv", mode="w", encoding="UTF-8").write(f) #сахраняю результат в новом файле
