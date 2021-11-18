from client import Client


class Admin:
    def __init__(self, admin):
        self.admin = admin

    def add_product(self):
        number_of_choice = "1"
        product_name = input("Введите название товара: ")
        cost_of_product = input("Введите стоимость товара: ")
        quantity = input("Введите количество штук товара: ")
        description = input("Введите описание товара: ")
        username = input("Введите логин: ")
        password = input("Введите пароль: ")
        self.admin.send(str.encode(
            str(number_of_choice + "," + product_name + "," + cost_of_product + "," + quantity
                + "," + description + "," + username + "," + password)))
        self.admin.close()


if __name__ == "__main__":
    admin = Admin(Client("127.0.0.1", 8888, timeout=5))
    admin.add_product()
