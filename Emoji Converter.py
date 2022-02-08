message = input("Masukkan Emot : ")
emoji_mapping = {
    ":]":  print("\N{grinning face}"),
    ":)":  print("\N{slightly smiling face}"),
    ":|":  print("\N{winking face}")
}
words = message.split(" ")
output = ""
for i in words: 
    output = output + emoji_mapping.get(i, i) + " "
print(output)

