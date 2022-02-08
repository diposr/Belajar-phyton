# Date and Time (latihan)

import datetime as dt

print("\n"+5*"="+"Tanggal Ya?"+5*"=")

hari_ini = dt.date.today()
print(hari_ini)

print("\n"+5*"="+"Kapan aku lahir?"+5*"=")

tanggal = dt.date(2004,11,10)
print(tanggal)

print("Silakan masukkan tanggal, Bulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t : "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Ini adalah tanggal lahir anda : {tanggal_lahir}")
print(f"Hari apa saya dilahirkan : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"umur anda adalah : {umur_tahun} tahun")
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Harinya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")



