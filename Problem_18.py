# Python program to store name,address,contact in dictionary and update contact.
dict={}
dict["name"]=input("Enter your name: ")
dict["address"]=input("Enter the address: ")
dict["contact"]=input("Enter your contact number: ")
print(dict)
# dict["contact"]=input("Enter the updated contact number: ")
dict.update({"updated_contact":input("Enter the updated contact number: ")})
print(dict)