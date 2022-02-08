# format string


# contoh generic
# string

nama = "Dipo"
format_str = f"hallo {nama}"
print(format_str)

# angka

angka = 2004
format_str = f"angka = {angka}"
print(format_str)

# boolean

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat 

bilangan = 15
format_str = f"bilangan bulat {bilangan:d}"
print(format_str)

# bilangan dengan ordo ribuan

ribuan = 3000
format_str = f"ribuan = {ribuan:,}"
print(format_str)

# bilangan decimal

decimal = 35.467
format_str = f"decimal = {decimal:.2f}"
print(format_str)

# menampilkan leading zero

leading = 35.467
format_str = f"leading = {leading:010.2f}"
print(format_str)


# menampilkan tanda + dan - 
angka_minus = -10
angka_plus = +10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:-d}"

print(format_minus)
print(format_plus)

# memformat persen

persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan aritmatika di dalam placeholder

harga = 10000
jumlah = 5

format_string = f"harga total = Rp {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hex)

angka = 255

format_binary = f"binary {bin(angka)}"
print(format_binary)
format_octal = f"octal {oct(angka)}"
print(format_octal)
format_hex = f"hex {hex(angka)}"
print(format_hex)