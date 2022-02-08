# (+, -. /, *, exit)
command = ""
while command != "exit":
    command = input("Masukkan perintah :")
    if command == "exit":
        break
    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Perintah tidak dikenali")
        continue
    a = int(input("Masukkan angka pertama :"))
    b = int(input("Masukkan angka kedua :"))
    if command == "+":
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b
    print(f"Hasil : {result}")
    break
print("Terimakasih telah memakai aplikasi kami")



