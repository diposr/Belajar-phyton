# operasi dan manipulasi string

# 1. menyabung string (concatenate)

nama_pertama = 'Dipo'
nama_kedua = 'Syahid'
nama_ketiga = 'Ramadhan'

nama_lengkap = nama_pertama + " " + nama_kedua + " " + nama_ketiga
print(nama_lengkap)

# 2. menghitung panjang string

panjang = len(nama_lengkap)
print("berapa panjang string yang ada di " + nama_lengkap + " = " +str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di dalam string

d = "d"      # d adalah string d
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"     
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"     
status = d  not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string

print("wk"*5)
print(10*"wk")

# indexing
# dimulai dari 0 bukan 1 

print("index ke-0 : " + nama_lengkap[0])
print("index ke-8 : " + nama_lengkap[8])
print("index ke- -1 : " + nama_lengkap[-1])
# perbandingan angka dibelakang harus ditambah satu agar sesuai dengan perintah
print("index ke [0:4] : " + nama_lengkap[0:5])
print("index ke [0,2,4,6,8] : " + nama_lengkap[0:8:2])

# item paling kecil (min)
print("item yang paling kecil : " + min(nama_lengkap))

# item paling besar (max)
print("item paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("character untuk ascii 117 adalah : " + chr(data))

# 4. operator dalam method

data = "dipo syahid ramadhan"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))




