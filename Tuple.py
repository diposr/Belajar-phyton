# perbedaan list dengan tuple adalah jika list bisa diubah sedangkan tuple immutable
# tuple menggunakan () sedangkan list menggunakan []
# bila di list kita bisa menambahkan element sedangkan di tuple tidak bisa 

numbers = [8, 6, 5, 7, 9, 4] # ini termasuk tipe data collection karena memiliki banyak nilai 
print('Tanpa Diganti\n')
print(numbers)
print('\nSetelah Diganti\n')
numbers[0] = 11
print(numbers)

print('\nMenggunakan Tuple\n')
print(numbers[2])