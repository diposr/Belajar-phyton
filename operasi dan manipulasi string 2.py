# operator dalam dalam bentuk methods

## merubah case dari string

# mengubah semua ke-upper case

salam = "bro!"
print("normal = " + salam)

salam = salam.upper()
print("upper = " + salam)

# kitqa bisa mengubah semua ke lower case

a = "Ngakack AbiEss Pack"
print("normal = " + a)
a = a.lower()
print("lower = " + a)

# pengecekan dengan menggunakan isX method

# contoh untuk pengecekkan lower case

salam = 'AA'
apakah_lower = salam.islower() # hasilnya adalah boolean
print(salam + " is lower =" + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper =" + str(apakah_upper))

# isalpha() <--- untuk mengecek semua huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <--- spasi, tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf besar

judul = "Dipo Syahid Ramadhan"
apakah_judul = judul.istitle()
print(judul + " is judul = " + str(apakah_judul))

## mengecek komponen startswith() dan endswith() <-- keren abis
cek_start = "Dipo Syahid".startswith("Dipo")
print("Start = " + str(cek_start))

cek_ends = "Dipo Syhid Ramadhan".endswith("Ramadhan")
print("Ends = " + str(cek_ends))

# penggabungan komponen join() dan split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print("gabungan = " + str(gabungan))

# menjadi spasi
gabungan = ' '.join(pisah)
print("gabungan = " + str(gabungan))

gabungan = ' ehm '.join(pisah)
print("gabungan = " + str(gabungan))

# split
gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(20)
print("'"+kanan+"'")

kiri = "kiri".ljust(20)
print("'"+kiri+"'")
 
tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikkannya strip()
tengah = "tengah".strip("-")
print("'"+tengah+"'")






