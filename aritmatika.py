# operasi aritmatika

a = 20
b = 3

# operasi tambahan +

total = a + b
print (a, '+', b, '=', total)


# operasi pengurangan -

total = a - b
print (a, '-', b, '=', total)

# operasi perkalian *

total = a * b
print (a, '*', b, '=', total)

# operasi pembagian /

total = a / b
print (a, '/', b, '=', total)

# operasi ekponen(pangkat) **

total = a ** b
print (a, '**', b, '=', total)

# operasi modulus(sisa pembagian) %

total = a % b
print (a, '%', b, '=', total)

# floor division // (pembulatan dari operasi pembagian)

total = a // b
print (a,'//',b,'=',total)

# prioritas operasi, operation precedent

x = 5 
y = 6 
z = 7

hasil = x ** z * x // y ** x
print (x,'**',z,'*',x,'//',y,'**',x,'=',hasil)


hasil = (x + y) * z
print ('(',x,'+',y,') *',z,'=',hasil)

# prioritas operasi 
'''
  1. ()
  2. eksponen **
  3. perkalian dan teman teman * / // % 
  4. pertambahan dan pengurangan + -
'''

