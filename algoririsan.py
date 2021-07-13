#belajar menggunakan algoritma menggunakan intersectio function pada python


def cari_irisan(lis1, lis2):
    set1 = set(lis1)
    set2 = set(lis2)

    return list(set1.intersection(set2))

lis1 = [20, 10, 23, 22, 45, 90, 19]
lis2 = [12,1,20, 23,45, 90, 20, 21, 19]
new_list = cari_irisan(lis1, lis2)
print(new_list)