# Name: Ivy Loi
# Date: 10/27/25
# Purpose of file: Create functions that are to be implemented in main.py

import json
import os # used for set_name function

class Contacts:

    def __init__(self, /, *, filename):
        ''' initializing member variables'''
        self.f = filename
        self.emD = {}
        try:
            with open(self.f, 'r') as file:
                self.emD = json.load(file)
        except FileNotFoundError:
           pass

    def add_contact(self, /, *, id, first_name, last_name):
        ''' adds contact to system '''
        if id in self.emD:
            return "error"
        self.emD[id] = [first_name, last_name]
        self.emD = dict(sorted(self.emD.items(), key = lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.f, 'w') as file:
            json.dump(self.emD, file)
        return {id: self.emD[id]}
    
    def modify_contact(self, /, *, id, first_name, last_name):
        ''' modifies contact in system '''
        if id not in self.emD:
            return "error"
        self.emD[id] = [first_name, last_name]
        self.emD = dict(sorted(self.emD.items(), key = lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.f, 'w') as file:
            json.dump(self.emD, file)
        return {id: self.emD[id]}
    
    def delete_contact(self, /, *, id):
        ''' deletes contact entered '''
        if id not in self.emD:
            return "error"
        del_c = {id: self.emD[id]}
        del self.emD[id]
        with open(self.f, 'w') as file:
            json.dump(self.emD, file)
        
        return del_c
    
    def print_contact(self): 
        ''' prints out sorted contact list '''
        if not self.emD:
            print("There are no contacts in the system currently, add some in first.")
            return "error"
        else:
            print("==================== CONTACT LIST ====================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for id, (first_name, last_name) in sorted(self.emD.items(), key=lambda item: (item[1][1], item[1][0])):
                print(f"{last_name:<22}{first_name:<22}{id}")

    def set_name(self, *, name):
        ''' sets name of file inputted'''
        if not name.strip(): # Error check used to check if user entered empty file name
            print("Filename cannot be empty.")
            return "error"
        # Checking to see if directory is not empty and doesn't exist on disk
        directory = os.path.dirname(name)
        if directory and not os.path.exists(directory):
            print("Directory does not exist.")
            return "error"
        self.f = name

    def valid_phone(self, *, id):
        ''' Edge case function that checks if phone number entered is valid'''
        return id.isdigit() and len(id) == 10
    
    def valid_first(self, *, first):
        ''' Edge case that checks if first name is valid '''
        first = first.strip()
        if not first:
            print("First name entered is just a space, this is invalid, returning to main menu.")
            return "error"
        
    def valid_last(self, *, last):
        ''' Edge case that checks if lst name is valid '''
        last = last.strip()
        if not last:
            print("Last name entered is just a space, this is invalid, returing to main menu.")
            return "error"