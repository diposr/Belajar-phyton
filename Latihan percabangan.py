# Latihan percabangan 

# kalkulator sederhana

print(20*"=")
print("Kalkulator sederhana")
print(20*"=")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,x,/) :")
angka_2 = float(input("masukkan angak 2 = "))

# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
elif operator == "-":
    hasil = angka_1 - angka_2
elif operator == "/":
    hasil = angka_1 / angka_2
elif operator == "x":
    hasil = angka_1 * angka_2
else:
    print("Maaf kami tidak bisa mendeteksi permintaan anda")
print("ini lah hasilnya = " + str(hasil))





