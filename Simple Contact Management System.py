import json

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact's name: ")
    phone = input("Enter contact's phone number: ")
    email = input("Enter contact's email address: ")
    
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)
    print(f"{name} has been added to your contacts.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("You have no contacts yet.")
    else:
        print("Your Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact}: {contacts[contact]['Phone']} | {contacts[contact]['Email']}")

# Function to edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    if contacts:
        choice = int(input("Enter the number of the contact you want to edit: "))
        contact_to_edit = list(contacts.keys())[choice - 1]
        print(f"Editing {contact_to_edit}:")
        new_phone = input("Enter new phone number (press Enter to keep current): ")
        new_email = input("Enter new email address (press Enter to keep current): ")
        
        if new_phone:
            contacts[contact_to_edit]["Phone"] = new_phone
        if new_email:
            contacts[contact_to_edit]["Email"] = new_email
        
        save_contacts(contacts)
        print(f"{contact_to_edit} has been updated.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        choice = int(input("Enter the number of the contact you want to delete: "))
        contact_to_delete = list(contacts.keys())[choice - 1]
        del contacts[contact_to_delete]
        save_contacts(contacts)
        print(f"{contact_to_delete} has been deleted from your contacts.")

# Main function
def contact_management():
    contacts = load_contacts()
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Edit a Contact")
        print("4. Delete a Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the contact management system
contact_management()
