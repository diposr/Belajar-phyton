# latihan perulangan membuat segitiga

sisi = 10
# dummy variable
print("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("akhir dari for\n")

print("awal dari while")
count = 1
while True:
    print("*"*count)
    count +=1
    if count > sisi:
        break
print("akhir dari while\n")

# hanya ganjil saja
count = 1
print("awal ganjil dan genap")
while True:
    # akan kembali ke atas jika ganjil
    if count%2:
        count += 1
        continue
    # akan print jika genap
    else:
        print("*"*count)
        count += 1
    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("akhir dari program")

# membuat segitiga
print("membuat segitiga")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("akhir dari program\n")

# membuat belat ketupat
print("membuat segitiga\n")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
count=sisi
spasi=1
while True:
    if count==sisi:
        count-=1
        continue
    elif (count%2):
        print(" "*spasi,"*"*count)
        count-=1
        spasi+=1
    else:
        count-=1
    if count==0:
        break

    
    
