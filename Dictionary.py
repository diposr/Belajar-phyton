# Dictionary adalah sebuah struktur data yang data minyimpan data dalam bentuk key dan value artinya adalah pasangan antara kunci dan nilai
# Dictionary di pyhton dilambangkan dengan tanda kurung kurawal {}

user = {
    "name" : "Dipo Syahid Ramadhan",
    "age" : 17,
    "is_admin" : True
}
user["username"] = "Dipo Syahid Ramadhan"
user["name"] = "Dipo S"
temp = user.get('name')
print(temp)
