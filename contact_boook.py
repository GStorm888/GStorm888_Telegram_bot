class UserContact:
    def __init__(self,
                name: str,
                phone_number: str = "",
                description: str = "",
                ):
        self.name = name
        self.phone_numder = phone_number
        self.description = description

    def set_phone_number(self, phone_number: str):
        self.phone_numder = phone_number

    def set_description(self, description: str):
        self.description = description


    def __str__(self):
        return f"Имя: {self.name}, номер телефона: {self.phone_numder}, описание: {self.description}"
    
class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact:UserContact):
        self.contacts.append(contact)

    def search(self, name):
        found_contacts = []
        for contact in self.contacts:
            if contact.name == name:
                return found_contacts

    def get_contacts(self):
        return self.contacts


class ContactBuilder:

    def __init__(self):
        self.current_contact = {}
        self.saved_contacts = {}

    def get_contacts(self, chat_id):
        if chat_id not in self.saved_contacts:
            return []
        return self.saved_contacts[chat_id].get_contacts()

    def add_name(self, chat_id, name):
        self.current_contact[chat_id] = UserContact(name)

    def add_phone_number(self, chat_id, phone_number: str):
        self.current_contact[chat_id].set_phone_number(phone_number)

    def add_description(self, chat_id, description: str):
        self.current_contact[chat_id].set_description(description)

    def build(self, chat_id):
        current_contact = self.current_contact[chat_id]

        if chat_id not in self.saved_contacts:
            self.saved_contacts[chat_id] = ContactBook()

        self.saved_contacts[chat_id].add_contact(current_contact)

        del self.current_contact[chat_id]

