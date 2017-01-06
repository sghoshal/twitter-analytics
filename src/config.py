# Kafka Configurations

TOPIC = 'topic-soum'
KAFKA_SERVER = 'localhost:9092'

# Spark Configurations

BATCH_INTERVAL = 5

# Configure window params. 
# The window size and slide interval has to be a mulitple of batch interval. 
WINDOW_SIZE = 60
SLIDE_INTERVAL = 30

SPARK_CHECKPOINT_DIR = '/Users/soum/Projects/twitter-analytics/spark-stream-checkpoint'