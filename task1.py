import re

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    additional_info = input("Enter additional information: ")

    contacts[phone_number] = {'Name': name, 'Phone Number': phone_number, 'Email': email, 'Additional Info': additional_info}

def edit_contact():
    phone_number = input("Enter the phone number of the contact to edit: ")
    if phone_number in contacts:
        name = input("Enter the updated name: ")
        email = input("Enter the updated email address: ")
        additional_info = input("Enter the updated additional information: ")
        
        contacts[phone_number]['Name'] = name
        contacts[phone_number]['Email'] = email
        contacts[phone_number]['Additional Info'] = additional_info
    else:
        print("Contact not found.")

def delete_contact():
    phone_number = input("Enter the phone number of the contact to delete: ")
    if phone_number in contacts:
        del contacts[phone_number]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    phone_number = input("Enter the phone number of the contact to search for: ")
    if phone_number in contacts:
        print("Contact Details:")
        for key, value in contacts[phone_number].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def display_all_contacts():
    print("All Contacts:")
    for phone_number, contact in contacts.items():
        print(f"Phone Number: {phone_number}")
        for key, value in contact.items():
            print(f"{key}: {value}")
        print()

def export_contacts(filename):
    with open(filename, 'w') as file:
        for phone_number, contact in contacts.items():
            file.write(f"{phone_number},{contact['Name']},{contact['Email']},{contact['Additional Info']}\n")
    print("Contacts exported successfully.")

def import_contacts(filename):
    with open(filename, 'r') as file:
        for line in file:
            phone_number, name, email, additional_info = line.strip().split(',')
            contacts[phone_number] = {'Name': name, 'Email': email, 'Additional Info': additional_info}
    print("Contacts imported successfully.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            filename = input("Enter the filename to export contacts: ")
            export_contacts(filename)
        elif choice == '7':
            filename = input("Enter the filename to import contacts: ")
            import_contacts(filename)
        elif choice == '8':
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
