# Build a basic contact list using a dictionary. Initially, the dictionary can be empty.
# Allow users to add new contacts with names and phone numbers.
# Users should also be able to search for contacts by name and display their phone numbers(use in operator).

contacts = []
add_contacts = True
while add_contacts:
    add = input("Do you want to add another contact? y/n: ")
    if add == "y":
        name = input("enter name: ")
        number = input("enter phone number: ")
        contacts.append({"name":name, "number":number})
    else:
        break

print(contacts)
if len(contacts) > 0:       ##
    search_contact = input("Enter phone number to search for the contact: ")
    contact_found = False
    for contact in contacts:
        if contact["number"] == search_contact:
            print("Name: ", contact["name"])
            print("Number: ", contact["number"])
            contact_found=True
            break
    if not contact_found:
        print("Contact not found")
else:
    print("Contacts list is empty")
