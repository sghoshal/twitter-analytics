# Keys and tokens for Twitter API.

ACCESS_TOKEN = "3377676014-ZmjDINws5x7aqW9KETOXzEAx0gthou0xD2zNCj2"
ACCESS_TOKEN_SECRET = "tXrm2Hdpi6by28U6pH4nnNio8Zmp7gIsfdE1gGNaAJYUL"
CONSUMER_KEY = "92vL5Z0rr0WH5zvYHQawpOzr3"
CONSUMER_SECRET = "IksT7MeNYROfl0r2OlL7CFFK0RV40Ann7NY9W6AXGQv540h6k0"

# Kafka topic

TOPIC = 'topic-soum'
KAFKA_SERVER='localhost:9092'

# SPARK CONFIG

BATCH_INTERVAL = 5
# Configure window params. 
# The window size and slide interval has to be a mulitple of batch interval. 
WINDOW_SIZE = 60
SLIDE_INTERVAL = 30