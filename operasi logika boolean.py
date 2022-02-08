# operasi logika atau boolean

# not, or, and, nor

print('===NOT===')
a = True
c = not a

print('data a =',a)
print('--------NOT')
print('data c =',c)

# OR
print('===OR===')
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

#  OR (Jika salah satu adalah true makan akan menjadi True)(seperti ditambah)

# AND

print('===AND===')
a = True
b = False
c = a and b
print(a,'and',b,'=',c)

a = True
b = True
c = a and b
print(a,'and',b,'=',c)

a = False
b = False
c = a and b
print(a,'and',b,'=',c)

a = False
b = True
c = a and b
print(a,'and',b,'=',c)

# AND (Jika dua buah nilai true maka hasil true) (seperti dikalikan)

# XOR

print('===XOR===')
a = True
b = False
c = a ^ b
print(a,'^',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'^',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'^',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'^',b,'=',c)

# XOR (akan true jika salah satu true sisanya false)