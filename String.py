

# string adalah kumpulan dari karakter
# "i"  <- ini adalah karakter i 

data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
  1. dengan membuat single quote (')
'''

data = 'Menggunakan single quote'
print(data)

'''
  2 . cara membuat double qoute (")
'''

data = "Menggunakan double quote"
print(data)

# menggunakan dua duanya

print('"Hallo, apa kabar?"')
print(" 'Halo, apa kabar?' ")

# karena si jum'at menggunkan tanda kutip didalamnya makanya memakai tanda kutip dua
print("ini adalah hari jum'at")

# 2. Membuat tanda \ 
# tanda [\] dibuat sebelum karakter khusus

# Membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash

# ("C:\User\Ucup") disebut seabagi folder
# bagaimana backlash diprint sebagai backlash?
# adalah dengan menamabahkan sebuah backlash lagi

print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, semakin jauh")

# backspace
print("Ucup \botong, jadi deketan")

# newline
print("ini barus pertama.\nini baris kedua")

# 3. string literal atau raw

# hati-hati
print('C:\new folder')

# menggunakan raw string
print(r'C:\new folder')

# menggunakan literal string

print("""
 Nama : Dipo
 Kelas : XI IPA 3
""")

# multiline literal string dan raw
print(r"""
 Nama : Dipo
 Kelas : XI IPA 3
 Lahir : 10 november 2004

""")




