from contacts import Contacts

filename = "contacts.json"

choices = ["1", "2", "3", "4", "5", "6"]

while True:
    print("      *** TUFFY TITAN CONTACT MAIN MENU")
    print()
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Set contact filename")
    print("6. Exit the program")
    print()
    prompt = input("Enter menu choice: ")
    if prompt == "1":
        phone = input("Enter phone number: ")
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        add = contacts.add_contact(id=phone, first_name=first, last_name=last)
        if add == "error":
            print("Error, this contact already exists in the system")
        else:
            print("Added: ", add)
    elif prompt == "2":
        phone = input("Enter phone number: ")
        nfirst = input("Enter first name: ")
        nlast = input("Enter last name: ")
        mod = contacts.modify_contact(id=phone, nfirst_name=nfirst, nlast_name=nlast)
        if mod == "error":
            print("Error, the phone number entered does not exist in the system")
        else:
            print("Modified: ", mod)
    elif prompt == "3":
        phone = input("Enter phone number: ")
        delp = contacts.delete_contact(id=phone)
        if delp == "error":
            print("Error, the phone number entered does not exist in the system")
        else:
            print("Deleted: ", delp)
    elif prompt == "4":
        contacts.print_contact()
    elif prompt == "5":
        filename = input("Enter new filename: ")
        contacts = Contacts(filename=filename)
        print(f"Filename set to {filename}")
    elif prompt == "6":
        break
    if prompt not in choices:
        print("Invalid option, try again")
        continue
        