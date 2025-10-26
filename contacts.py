import json
import os

class Contacts:

    def __init__(self, /, *, filename):
        self.f = filename
        self.emD = {}
        try:
            with open(self.f, 'r') as file:
                self.emD = json.load(file)
        except FileNotFoundError:
           pass

    def add_contact(self, /, *, id, first_name, last_name):
        if id in self.emD:
            return "error"
        self.emD[id] = [first_name, last_name]
        self.emD = dict(sorted(self.emD.items(), key = lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.f, 'w') as file:
            print("Writing to", self.f)
            json.dump(self.emD, file)
        return {id: self.emD[id]}
    
    def modify_contact(self, /, *, id, first_name, last_name):
        if id not in self.emD:
            return "error"
        self.emD[id] = [first_name, last_name]
        self.emD = dict(sorted(self.emD.items(), key = lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.f, 'w') as file:
            json.dump(self.emD, file)
        return {id: self.emD[id]}
    
    def delete_contact(self, /, *, id):
        if id not in self.emD:
            return "error"
        del_c = {id: self.emD[id]}
        del self.emD[id]
        with open(self.f, 'w') as file:
            json.dump(self.emD, file)
        
        return del_c
    
    def print_contact(self): 
        if not self.emD:
            print("There are no contacts in the system currently, add some in first.\n")
            return "error"
        else:
            print("==================== CONTACT LIST ====================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for id, (first_name, last_name) in sorted(self.emD.items(), key=lambda item: (item[1][1], item[1][0])):
                print(f"{last_name:<22}{first_name:<22}{id}")

    def set_name(self, *, name):
        if not name.strip():
            print("Filename cannot be empty.")
            return
        directory = os.path.dirname(name)
        if directory and not os.path.exists(directory):
            print("Directory does not exist.")
            return
        self.f = name

    def valid_phone(self, *, id):
        return id.isdigit() and len(id) == 10
    