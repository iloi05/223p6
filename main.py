from contacts import Contacts


filename = "contacts.json"
contacts = Contacts(filename=filename)


choices = ["1", "2", "3", "4", "5", "6"]

while True:
    print()
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
    print()
    if prompt == "1":
        id = input("Enter phone number: ").strip()
        clean = ''.join(filter(str.isdigit, id))
        if not contacts.valid_phone(id=clean):
            print("That is not a valid phone number ... returning to main menu")
            continue
        else:    
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            add = contacts.add_contact(id=id, first_name=first, last_name=last)
            if add == "error":
                print("Error, this contact already exists in the system")
            else:
                print(f"Added: {first} {last}.")
    elif prompt == "2":
        id = input("Enter phone number: ")
        clean = ''.join(filter(str.isdigit, id))
        if not contacts.valid_phone(id=clean):
            print("That is not a valid phone number... returning to main menu")
            continue
        else:
            nfirst = input("Enter first name: ")
            nlast = input("Enter last name: ")
            mod = contacts.modify_contact(id=clean, first_name=nfirst, last_name=nlast)
        if mod == "error":
            print("Error, the phone number entered does not exist in the system")
            continue
        else:
            print(f"Modified: {nfirst} {nlast}.")
    elif prompt == "3":
        id = input("Enter phone number: ")
        clean = ''.join(filter(str.isdigit, id))
        if not contacts.valid_phone(id=clean):
            print("That is not a valid phone number... returning to main menu")
            continue
        delp = contacts.delete_contact(id=clean)
        if delp == "error":
            print("Error, the phone number entered does not exist in the system")
        else:
            first, last = delp[clean]
            print(f"Deleted: {first} {last}")
    elif prompt == "4":
        contacts.print_contact()
    elif prompt == "5":
        filename = input("Enter new filename: ")
        contacts.set_name(name=filename)
        print(f"Filename set to {filename}")
    elif prompt == "6":
        break
    if prompt not in choices:
        print("Invalid option, try again")
        continue
        