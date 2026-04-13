import json

def display_menu():
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit\n")
def add_contact(contact_book):
        name = input(("Insert the name of the new contact: "))
        if name in contact_book:
                print("Contact already exists!\n")
        else:
                phone = input("Please insert the phone number: ")
                email = input("Please insert the e-mail: ")
                address = input("Please inser the address: ")
                contact_book[name] = {
                        "phone" : phone,
                        "email" : email,
                        "address" : address
                }
                save_contacts(contact_book)
                print("Contact added successfully!\n")
def view_contact(contact_book):
        name = input("Enter the name to be searched:")
        if name in contact_book:
                contact = contact_book[name]
                print(f"\nName: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"E-mail: {contact['email']}")
                print(f"Address: {contact['address']}\n")
        else:
                print("Contact not found!\n")
def edit_contact(contact_book):
        name = input("Insert the name of the contact to be edited:")
        if name in contact_book:
                contact_book[name]["phone"] = input("\nInsert new number: ")
                contact_book[name]["email"] = input("Insert new e-mail: ")
                contact_book[name]["address"] = input("Insert new address: ")
                save_contacts(contact_book)
                print("Contact updated successfully!\n")
        else:
                print("Contact not found!\n")
def delete_contact (contact_book):
        name = input("Insert the name of the contact to be deleted: ")
        if name in contact_book:
                del contact_book[name]
                save_contacts(contact_book)
                print("Contact deleted successfully!\n")
        else:
                print("Contact not found!\n")
def list_all_contacts(contact_book):
        if not contact_book:
                print("No contacts available.\n")
        else:
                for name, contact in contact_book.items():
                        print(f"Name: {name}")
                        print(f"Phone: {contact['phone']}")
                        print(f"E-mail: {contact['email']}")
                        print(f"Address: {contact['address']}\n")
def save_contacts(contact_book):
        with open("contacts.json", "w") as f:
                json.dump(contact_book, f, indent=4)
def load_contacts():
        try:
                with open("contacts.json", "r") as f:
                        return json.load(f)
        except FileNotFoundError:
                return{}
contact_book = load_contacts()
while True:
        display_menu()
        choice = input(" Choose your option: ")
        if choice == "1":
                add_contact(contact_book)
        elif choice == "2":
                view_contact(contact_book)
        elif choice == "3":
                edit_contact(contact_book)
        elif choice == "4":
                delete_contact(contact_book)
        elif choice == "5":
                list_all_contacts(contact_book)
        elif choice == "6":
                print("Exiting program... Goodbye!")
                break
        else:
                print("Invalid choice. Please try again.")
