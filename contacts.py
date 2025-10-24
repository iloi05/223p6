import json

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
        sorted(self.emD.items(), key = lambda item: (item[1][1], item[1][0]))
        with open(self.f, 'w') as file:
            print("Writing to", self.f)
            json.dump(self.emD, file)
        return {id: self.emD[id]}
    
    def modify_contact(self, /, *, id, nfirst_name, nlast_name):
        if id not in self.emD:
            return "error"
        self.emd[id] = [nfirst_name, nlast_name]
        sorted(self.emD.items(), key = lambda item: (item[1][1], item[1][0]))
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
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for id, (first_name, last_name) in sorted(self.emD.items(), key=lambda item: (item[1][1], item[1][0])):
            print(f"{last_name:<22}{first_name:<22}{id}")

    def set_name(self, *, name):
        self.f = name

    def valid_phone(self, *, id):
        return id.isdigit()