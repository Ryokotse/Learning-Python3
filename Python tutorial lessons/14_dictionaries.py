#Dictionaries

#customer = {
#    "name": "John Smith",
#    "age": 30,
#    "is_verified": True
#}
#customer["name"] = "Jack Smith"
#print(customer["name"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
