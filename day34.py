

user_input = input("Enter the name: ")

dict1 = {
    "Mohamed" : "123",
    "Essam"  : "456",
    "Sadek"    : "789"
}

for i in dict1.keys():
    if user_input in i:
        print (dict1[i])