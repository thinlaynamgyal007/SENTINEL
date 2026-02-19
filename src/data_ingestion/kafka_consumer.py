import json
import kafka

class KafkaDataConsumer:
    def __init__(self, topic, bootstrap_servers):
        self.topic = topic
        self.consumer = kafka.KafkaConsumer(self.topic, bootstrap_servers=bootstrap_servers)

    def consume_messages(self):
        for message in self.consumer:
            yield json.loads(message.value)


class IoTDataConnector:
    def __init__(self, kafka_topic, bootstrap_servers):
        self.consumer = KafkaDataConsumer(kafka_topic, bootstrap_servers)

    def get_data(self):
        data = []
        for message in self.consumer.consume_messages():
            data.append(message)
        return data
