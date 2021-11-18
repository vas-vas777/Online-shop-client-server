import asyncio
from dz3 import Product, Order

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        data_from_client = data.decode().split(',')
        # print(data_from_client)
        if data_from_client[0] == "4":
            username = data_from_client[1]
            password = data_from_client[2]
            product_name = data_from_client[3]
            count_products = data_from_client[4]
            order = Order()
            status = order.make_order(username, password, product_name, count_products)
            self.transport.write(str.encode(status))
            self.eof_received()
        elif data_from_client[0] == "7":
            username = data_from_client[1]
            password = data_from_client[2]
            product_name = data_from_client[3]
            count_products = data_from_client[4]
            order = Order()
            status = order.add_product_to_existing_order(username, password, product_name, count_products)
            self.transport.write(str.encode(status))
            self.eof_received()
        elif data_from_client[0] == "2":
            product_name = data_from_client[1]
            product = Product(product_name)
            status = product.print_information_about_product()
            # print(status)
            send_data = ""
            send_data += status[0] + " "
            print(type(status))
            if isinstance(status,str):
                self.transport.write(str.encode(status))
                self.eof_received()
            else:
                for count in range(len(status[1])):
                    send_data += status[1][count]
                    if count < 2:
                        send_data += " "
                # print(send_data)
                self.transport.write(str.encode(send_data))
                self.eof_received()
        elif data_from_client[0] == "3":
            # product_name=data_from_client[1]
            product = Product()
            status = product.print_about_products()
            # print(status)
            for line in status:
                self.transport.write(str.encode(line + "\n"))
            self.eof_received()
        elif data_from_client[0] == "5":
            username = data_from_client[1]
            password = data_from_client[2]
            order = Order()
            status = order.check_order(username, password)
            # print(status)
            send_data = ""
            for key, value in status[1].items():
                send_data += status[0] + " "
                send_data += key + " " + value[0] + " " + value[1] + "\n"
                self.transport.write(str.encode(send_data))
                send_data = ""
            self.eof_received()
        elif data_from_client[0] == "6":
            username = data_from_client[1]
            password = data_from_client[2]
            order = Order()
            status = order.pay_for_order(username, password)
            # print(status)
            self.transport.write(str.encode(status))
            self.eof_received()
        elif data_from_client[0] == "1":
            print(data_from_client)
            product_name = data_from_client[1]
            cost_of_product = data_from_client[2]
            quantity = data_from_client[3]
            description = data_from_client[4]
            username = data_from_client[5]
            password = data_from_client[6]
            Product(product_name, cost_of_product, quantity, description, username, password)
            self.eof_received()

    # def _connection_lost(self, exception):
    #     self.transport.close()


def run_loop(host, port):
    loop = asyncio.get_event_loop()
    # Each client connection will create a new protocol instance
    coro = loop.create_server(EchoServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    # print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


# def run_server(host='127.0.0.1', port=8888):
#     run_loop(host, port)

asyncio.run(run_loop('127.0.0.1', 8888))
"""
async def main(host, port):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        host, port)

    async with server:
        await server.serve_forever()

#def run_server(host='127.0.0.1', port=8888):
asyncio.run(main(host,port))
# asyncio.run(run_server())
# asyncio.run(run_server('127.0.0.1',8888))

# asyncio.run(run_server('127.0.0.1', 8888))
"""
