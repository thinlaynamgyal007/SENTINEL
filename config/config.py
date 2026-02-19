# Configuration settings for the SENTINEL Project

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'sentinel_data'

# Database Configuration
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_NAME = 'sentinel_db'

# API Endpoints
API_ENDPOINTS = {
    'data_fetch': 'http://localhost:5000/data',
    'anomaly_detection': 'http://localhost:5000/anomaly'
}

# Anomaly Detection Parameters
ANOMALY_DETECTION_THRESHOLD = 0.05
ANOMALY_DETECTION_METHOD = 'DBSCAN'
