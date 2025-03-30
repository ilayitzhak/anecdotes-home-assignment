from plugin import Plugin


class SendDataPlugin(Plugin):
    def __init__(self, data):
        self.data = data

    def send(self):
        # Simulate sending data
        print(f"Sending data: {self.data}")
        return True

    def receive(self):
        # Simulate receiving data
        received_data = f"Received: {self.data}"
        print(received_data)
        return received_data