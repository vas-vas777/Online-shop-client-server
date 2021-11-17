from client import Client


def run(host, port):
    admin = Client(host, port, timeout=5)
    number_of_choice = "1"
    product_name = "шкаф"
    cost_of_product = "10000"
    quantity = "11"
    description = "шкаф для одежды"
    username = "admin"
    password = "1234"
    admin.send(str.encode(
        str(number_of_choice + "," + product_name + "," + cost_of_product + "," + quantity
            + "," + description + "," + username + "," + password)))


if __name__ == "__main__":
    run("127.0.0.1", 8888)