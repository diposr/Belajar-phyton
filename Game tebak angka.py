trying = 0
secret_number = 5
limit = 3
while trying < limit:
    guess_number = input("Masukkan angka (0-9) :")
    guess_number = int(guess_number)
    if guess_number == secret_number:
        print("\nSelamat Anda Benar\n")
        break
    else:
        print("Ayo coba lagi")
trying += 1
