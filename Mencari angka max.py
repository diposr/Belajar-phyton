numbers = [1, 3, 2, 5, 8, 7]
total = sum(numbers)
print(total)

# menemukan angka yang paling besar di dalam integer

# cara pertama
max_number = max(numbers)
print(max_number)

# cara kedua
numbers.sort()
max_number = numbers[-1]
print(max_number)

# cara ketiga
max_number = numbers[0] # kita mengambil elemen pertama yang ada di numbers
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)
 