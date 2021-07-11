# belajar menggunakan fungsi zip pada python
# fungsi zip digunakan jika akan menggabungkan dua list seperti layaknya dictionary


movie=["Cinta", "Habibi", "Rambo", "AADC"]
rating=[4,8, 7, 10]
new_list = []

for rate in zip(movie, rating):
    new_list.append(rate)
print(new_list)

