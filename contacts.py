# preparing contact book 
'''
1.adding contact
2.viewing all contacts which are present in the contact book
3.searching contact
4.deleting contact successfully
'''


contacts = {"names": ['sai', "yashu"], 
            "phone": ["12345", "678910"]}

print("CONTACT BOOK")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Delete Contact")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    
    contacts["names"].append(name)
    contacts["phone"].append(phone)

    print(f"Contact with {name} added successfully")

elif choice == "2":
    for i in range(len(contacts["names"])):
        print(contacts["names"][i], ":", contacts["phone"][i])

elif choice == "3":
    name = input("Enter name to search: ")
    
    if name in contacts["names"]:
        index = contacts["names"].index(name)
        print("Phone number:", contacts["phone"][index])
    else:
        print(f"Contact with {name} not found.")

elif choice == "4":
    name = input("Enter name to delete: ")
    
    if name in contacts["names"]:
        index = contacts["names"].index(name)
        contacts["names"].pop(index)
        contacts["phone"].pop(index)
        print(f"Contact with {name} deleted successfully")
    else:
        print(f"Contact with {name} not found.")

else:
    print("Invalid choice.")