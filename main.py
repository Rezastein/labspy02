a = int(input("masukan bilangan a : "))
b = int(input("masukan bilangan b : "))
c = int(input("masukan bilangan c : "))

print (a, b, c)

if a > b:
    maks = a
else:
    maks = b
if c > maks:
    maks = c

print("Bilangan terbesar adalah : ", maks)