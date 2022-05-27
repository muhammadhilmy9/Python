#membuat decision habis dibagi2
x = int(input())
if x%2 == 0:
    print("genap")
else :
    print("Ganjil")

jam = int(input())

if jam >= 5 and jam <12:
    print("Selamat Pagi")
elif jam >= 12 and jam <15:
    print("Selamat Siang")
elif jam >= 15 and jam < 19:
    print("Selamat Sore")
else:
    print("Selamat Malam") 