from client import Client

class AsyncioClient:
    def __init__(self, client):
        self.client = client

    def run(self):
        # self.client = Client(host, port, timeout=15)
        # client2 = Client(host, port, timeout=5)
        while (True):
            number_of_choice = input("Введите 2 (Просмотреть информацию о товаре), \n"
                                     "Введите 3 (Посмотерть информацию о всех товарах), \n"
                                     "Введите 4 (Сделать заказ), \n"
                                     "Введите 5 (Узнать информацию о заказе), \n"
                                     "Введите 6 (Заплатить за заказ), \n"
                                     "Введите 7 (Добавить товар в заказ),\n"
                                     "Введите 0 (Для выхода): ")

            if number_of_choice == "4" or number_of_choice == "7":
                name = input("Введите логин: ")
                password = input("Введите пароль: ")
                product = input("Введите название товара: ")
                count_products = input("Количество товара: ")
                self.client.send(str.encode(
                    str(number_of_choice + "," + name + "," + password + "," + product + "," + count_products)))
            elif number_of_choice == "3":
                self.client.send(str.encode(str(number_of_choice)))
                print(self.client.read())
                continue
            elif number_of_choice == "2":
                product_name = input("Введите название товара: ")
                self.client.send(str.encode(str(number_of_choice + "," + product_name)))
                print(self.client.read())
                continue
            elif number_of_choice == "5" or number_of_choice == "6":
                name = input("Введите логин: ")
                password = input("Введите пароль: ")
                self.client.send(str.encode(str(number_of_choice + "," + name + "," + password)))
                print(self.client.read())
                continue
            elif number_of_choice == "0":
                self.client.close()
                break
            else:
                print("Неправильный ввод")
                self.client.close()
                break

            data = self.client.read()  # получение данных от сервера
            if data == "Заказ уже открыт":
                print(data, " Добавьте новые данные в заказ")
                name = input("Введите логин: ")
                password = input("Введите пароль: ")
                product = input("Введите название товара: ")
                count_products = input("Введите количество товара: ")
                number_of_choice = "7"
                self.client.send(str.encode(
                    str(number_of_choice + "," + name + "," + password + "," + product + "," + count_products)))
                data = self.client.read()
                print(data)
            elif data == "Заказ ещё не создан":
                print(data)
            elif data == "Введен не правильный пароль" or data == "Такого пользователя нет":
                print(data)
            elif data == "Такого продукта нет":
                print(data)
            elif data == "Заказ готов":
                print(data)
            continue


if __name__ == "__main__":
    client1 = AsyncioClient(Client("127.0.0.1", 8888))
    client1.run()
    # run("127.0.0.1", 8888)
