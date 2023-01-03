#contoh 1
angka = 1
while angka > 0 and angka < 11:
 angka = int(input("Masukkan angka antara 1-10: "))
 print("Kamu memasukkan angka", angka)

 
 #contoh 2
 angka = 1
while angka > 0 and angka < 11:
 angka = int(input("Masukkan angka antara 1-10: "))
if angka < 1 or angka > 10:
 print("Angka tidak valid.")
else:
 print("Kamu memasukkan angka", angka)


 #contoh 3
for i in range(10):

 print(i)

i = 0
while i < 10:
 print(i)
i = i + 1


 