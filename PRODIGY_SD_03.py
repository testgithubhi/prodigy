import json

class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        self.contacts.append({"Name": name, "Phone": phone, "Email": email})
        print("Contact added.")

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact['Name']}, {contact['Phone']}, {contact['Email']}")

    def edit_contact(self, index, name, phone, email):
        self.contacts[index - 1] = {"Name": name, "Phone": phone, "Email": email}
        print("Contact edited.")

    def delete_contact(self, index):
        del self.contacts[index - 1]
        print("Contact deleted.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
            print(f"Contacts saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
                print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print("File not found. No contacts loaded.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            contact_manager.add_contact(input("Name: "), input("Phone: "), input("Email: "))

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            contact_manager.edit_contact(int(input("Enter index to edit: ")), input("Name: "), input("Phone: "), input("Email: "))

        elif choice == '4':
            contact_manager.delete_contact(int(input("Enter index to delete: ")))

        elif choice == '5':
            contact_manager.save_to_file(input("Enter filename to save: "))

        elif choice == '6':
            contact_manager.load_from_file(input("Enter filename to load: "))

        elif choice == '7':
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number between 1 and 7.")

if _name_ == "_main_":
    main()