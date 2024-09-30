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
    