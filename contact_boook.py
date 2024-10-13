class UserContact:
    def __init__(self,
                name: str,
                phone_number: str,
                description:str = "",
                ):
        self.name = name
        self.phone_numder = phone_number
        self.description = description

    def __str__(self):
        return f"Имя: {self.name}, номер телефона: {self.phone_numder}, описание: {self.description}"
    
class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self,name: str,
                phone_number: str,
                description:str = "",):
        contact = UserContact(name, phone_number, description)
        self.contacts.append(contact)

    def search(self, name):
        found_contacts = []
        for contact in self.contacts:
            if contact.name == name:
                return found_contacts

    def get_contacts(self):
        return self.contacts


class ContactBilder:
    def add_name(self, name):
        ...

    def add_phone_number(self, phone_number):
        ...

    def add_description(self, description):
        ...

    def commit(self, description):
        ...