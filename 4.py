f = open("products.csv", encoding="UTF-8").read().split("\n")
f[0] = f[0] + ";promocode"
for i in range(1, len(f)):
    a = f[i].split(';')
    f[i] = f[i] + ";" + a[1][:2] + a[2][:2] + a[1][-1] + a[1][-2] + a[2][4] + a[2][3]
f = "\n".join(f)
open("product_promo.csv", mode="w", encoding="UTF-8").write(f)