class ContactBook:
    def __init__(self, contacts: dict):
        self.contacts = contacts
    
    def __len__(self):
        length_contacts = len([value for value in self.contacts])
        return length_contacts
    
    def __add__(self, other_contact: dict):
        if isinstance(other_contact, ContactBook):
            new_contacts = self.contacts | other_contact.contacts
            return new_contacts
        
    def __str__(self):
        return str(self.contacts)
    
    def __del__(self):
        print(f"The notebook was deleted!")
notebook_1 = ContactBook({'name':'nima', 'number': '125658'})
notebook_2 = ContactBook({'name': 'nazi', 'number': '565482'})
finall_dict = notebook_1 + notebook_2
print(notebook_1)
print(notebook_2)
print(finall_dict)
print(len(notebook_1))
print(len(notebook_2))
