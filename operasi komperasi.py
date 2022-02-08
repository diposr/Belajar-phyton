# operasi komparasi 

# setiap hasil dari operasi komperasi adalah

# >,<,>=,<=,==,!==,is,is not

a = 4
b = 2

# lebih besar dari >
print('=====')
hasil = a > 3
print(a,'>',3,"=",hasil)
hasil = b > 3
print(b,'>',3,"=",hasil)
hasil = b > 2
print(b,'>',2,"=",hasil)

# kurang dari <
print('=====')
hasil = a < 3
print(a,'<',3,"=",hasil)
hasil = b < 3
print(b,'<',3,"=",hasil)
hasil = b < 2
print(b,'<',2,"=",hasil)

# lebih dari sama dengan >=
print('=====')
hasil = a >= 3
print(a,'>=',3,"=",hasil)
hasil = b >= 3
print(b,'>=',3,"=",hasil)
hasil = b >= 2
print(b,'>=',2,"=",hasil)

# kurang dari sama dengan <=
print('=====')
hasil = a <= 3
print(a,'<=',3,"=",hasil)
hasil = b <= 3
print(b,'<=',3,"=",hasil)
hasil = b <= 2
print(b,'<=',2,"=",hasil)

# sama dengan ==
print('=====')
hasil = a == 3
print(a,'==',3,"=",hasil)
hasil = b == 3
print(b,'==',3,"=",hasil)
hasil = b == 2
print(b,'==',2,"=",hasil)

# tidak sama dengan !=
print('=====')
hasil = a != 3
print(a,'!=',3,"=",hasil)
hasil = b != 3
print(b,'!=',3,"=",hasil)
hasil = b != 2
print(b,'!=',2,"=",hasil)

# 'is' sebagai komparasi object identity
print('=====')
x = 5 # ini adalah assigment emembuat object 
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y 
print('x is y =',hasil)

# 'is not ' sebagai tidak sama dengan komparasi object identity
print('=====')
x = 5 # ini adalah assigment emembuat object 
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y 
print('x is not y =',hasil)





