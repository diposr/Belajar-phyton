# Width dan multiline

# Data

data_nama = "Dipo"
data_umur = 17
data_tinggi = 170
data_kaki = 43

# string standard

data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran kaki = {data_kaki}"
print(data_string)

# string multiline (dengan menggunkan newline, enter, \n)

print("\n"+5*"="+"DATA STRING"+5*"=")
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nukuran kaki = {data_kaki}"
print(data_string)

# string multiline (kutip triplets)
data_string = f"""nama = {data_nama} 
umur = {data_umur}
tinggi = {data_tinggi}
ukuran kaki = {data_kaki}"
"""
print("\n"+5*"="+"DATA STRING"+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama        = {data_nama} 
umur        = {data_umur}
tinggi      = {data_tinggi}
ukuran kaki = {data_kaki}
"""
print("\n"+5*"="+"DATA STRING"+5*"=")
print(data_string)