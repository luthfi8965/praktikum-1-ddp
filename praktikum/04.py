 # Latihan 1
hasil = 7 != 8
print(hasil)

hasil = 7 > 7.0
print(hasil)

hasil = 8.7 <= 8.70
print(hasil)


#latihan 2

hasil = True and True
print(hasil)

hasil = not(7 == 7.0)
print(hasil)

hasil = (2 > 3) or (9//2 != 4)
print(hasil)

hasil = (3 + True) / 2
print(hasil)


#latihan 3
number = 35

if number % 2 == 0:
    print('number is even')
else:
    print('number is odd')


#latihan 4
# x = 3 dan y = 4
x = 3
y = 4

if x % 2 == 0:
    print(x, 'is even')
else:
    print(x, 'is odd')

if y % 2 == 0:
    print(y, 'is even')
else:
    print(y, 'is odd')

# x = 2 dan y = 2
x = 2
y = 2

if x % 2 == 0:
    print(x, 'is even')
else:
    print(x, 'is odd')

if y % 2 == 0:
    print(y, 'is even')
else:
    print(y, 'is odd')

# x = 3 dan y = 2
x = 3
y = 2

if x % 2 == 0:
    print(x, 'is even')
else:
    print(x, 'is odd')

if y % 2 == 0:
    print(y, 'is even')
else:
    print(y, 'is odd')


#latihan 5
margin = True

width = 100 + (10 if margin else 2)
print(width)


#latihan 6
for i in range(1, 100):

 if (i % 2 == 0) and (i % 5 == 0):
  print(i,"adalah bilangan kelipatan 10")