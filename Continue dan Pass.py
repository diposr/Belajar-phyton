# continue, pass dan break

# pass -> dia berfunsi sebagai dummy, tidak akan dieksekusi

# continue

angka = 0 
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1
    if angka == 3:
        print("nice!")
        continue # akan membuat loop meloncat ke aksi 1
    print("whassup!") # aksi 2
print("Finish")
