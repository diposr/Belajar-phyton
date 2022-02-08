# Operasi biner / Operation binary

# (TRUE) dan (FALSE) kembali berlaku

# misal 2 = 00000010
#           -------- 
#           76543210 = 2^1 -> 2

# misal 1 = 00000001
#           --------
#           76543210 = 2^0 -> 1

a = 9 
b = 5

# bitwise OR (|)
c = a | b
print('\n===========OR========')
print('nilai :',a,' , binary :',format(a,'08b'))
# nilai 9 berasal dari penjumlahan operasi 00001001
#                                          --------
#                                          76543210 = 2^3 + 2^0 = 9
print('nilai :',b,' , binary :',format(b,'08b'))
print('======================= (|)')
print('nilai :',c,' , binary :',format(c,'08b'))
# nilai 13 berasal dari jumlah operasi a dan b (00001001 + 00000101)
#                                               00001001
#                                               00000101
#                                               --------+
#                                               00001101

# bitwise AND (&)
c = a & b
print('\n========AND========')
print('nilai :',a,' , binary :',format(a,'08b'))    
print('nilai :',b,' , binary :',format(b,'08b'))
print('======================= (&)')
print('nilai :',c,' , binary :',format(c,'08b'))
# nilai 1 berasal dari true dan false ( TRUE + TRUE = TRUE)

# bitwise XOR (^)
c = a ^ b
print('\n========XOR========')
print('nilai :',a,' , binary :',format(a,'08b'))    
print('nilai :',b,' , binary :',format(b,'08b'))
print('======================= (^)')
print('nilai :',c,' , binary :',format(c,'08b'))
# nilai 12 berasal dari true dan false ( TRUE + TRUE = FALSE)

# bitwise NOT (~)
c = ~a
print('\n=================NOT===========')
print('nilai :',a,' binary :',format(a,"08b"))
print('======================= (~)')
print('nilai :',c,' , binary :',format(c,'08b'))
# kenapa bisa minus karena kita punya 0 karena 0 tidak bisa minus jadi ia akan mengambil angka 1

# shifting

# shifting right (>>)
c = a >> 1
print('\n=================SHIFTING RIGHT===========')
print('nilai :',a,' binary :',format(a,"08b"))
print('======================= (>>)')
print('nilai :',c,' , binary :',format(c,'08b'))
# 00000100 di dapat dari pergeseran arah kekanan dari angka yang dimasukkan, yaitu 1 

# shifting left(<<)
c = a << 1
print('\n=================NOT===========')
print('nilai :',a,' binary :',format(a,"08b"))
print('======================= (<<)')
print('nilai :',c,' , binary :',format(c,'08b'))
