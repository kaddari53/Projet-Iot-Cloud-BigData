import csv
from cassandra.cluster import Cluster
from uuid import uuid4

CASSANDRA_KEYSPACE = "amazon"
CASSANDRA_TABLE = "reviews"
TRAIN_PATH = "./train.csv"  # Mettre à jour le chemin si nécessaire
TEST_PATH = "./test.csv"    # Mettre à jour le chemin si nécessaire

# Créer la table dans Cassandra
def create_table():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {CASSANDRA_KEYSPACE}
        WITH REPLICATION = {{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 }};
    """)
    session.execute(f"""
        CREATE TABLE IF NOT EXISTS {CASSANDRA_KEYSPACE}.{CASSANDRA_TABLE} (
            review_id UUID PRIMARY KEY,
            polarity INT,
            title TEXT,
            text TEXT
        );
    """)
    session.shutdown()
    cluster.shutdown()

# Charger les données dans Cassandra
def load_data_to_cassandra(file_path):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect(CASSANDRA_KEYSPACE)
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            session.execute(f"""
                INSERT INTO {CASSANDRA_TABLE} (review_id, polarity, title, text)
                VALUES (%s, %s, %s, %s)
            """, (uuid4(), int(row[0]), row[1], row[2]))
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    create_table()
    load_data_to_cassandra(TRAIN_PATH)
    load_data_to_cassandra(TEST_PATH)
