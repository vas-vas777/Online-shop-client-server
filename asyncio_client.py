import sys
from client import Client, ClientError
from dz3 import Order


def run(host, port):
    client1 = Client(host, port, timeout=15)
    client2 = Client(host, port, timeout=5)
    while(True):
        number_of_choice = input("Введите 2 (Просмотреть информацию о товаре), \n"
                       "Введите 3 (Посмотерть информацию о всех товарах), \n"
                       "Введите 4 (Сделать заказ), \n"
                       "Введите 5 (Узнать информацию о заказе), \n"
                       "Введите 6 (Заплатить за заказ), \n"
                       "Введите 7 (Добавить товар в заказ),\n"
                       "Введите 0 (Для выхода): ")

        if number_of_choice == "4" or number_of_choice == "7":
            name = "sas"
            password = "123"
            product = "стол"
            count_products = "1"
            client1.send(str.encode(str(number_of_choice + "," + name + "," + password + "," + product + "," + count_products)))
        elif number_of_choice == "3":
            client1.send(str.encode(str(number_of_choice)))
            print(client1.read())
            continue
        elif number_of_choice == "2":
            product_name = "стул"
            client1.send(str.encode(str(number_of_choice + "," + product_name)))
            print(client1.read())
            continue
        elif number_of_choice == "5" or number_of_choice == "6":
            name = "sas"
            password = "123"
            client1.send(str.encode(str(number_of_choice+","+name+","+password)))
            print(client1.read())
            continue
        elif number_of_choice == "0":
            client1.close()
            break
        else:
            print("Неправильный ввод")
            client1.close()
            break

        data = client1.read() #получение данных от сервера
        if data == "Заказ уже открыт":
            name = "vas"
            password = "123"
            product = "стул"
            count_products = "7"
            client1.send(str.encode(str(number_of_choice + "," + name + "," + password + "," + product + "," + count_products)))
            data = client1.read()
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
    run("127.0.0.1", 8888)
