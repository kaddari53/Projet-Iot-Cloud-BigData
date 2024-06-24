from cassandra.cluster import Cluster
from collections import defaultdict
import multiprocessing

CASSANDRA_KEYSPACE = "amazon"
CASSANDRA_TABLE = "reviews"

# Fonction Mapper
def mapper(document, n):
    words = document.split()
    word_count = defaultdict(int)
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        word_count[ngram] += 1
    return word_count

# Fonction Reducer
def reducer(mapped_results):
    final_counts = defaultdict(int)
    for counts in mapped_results:
        for ngram, count in counts.items():
            final_counts[ngram] += count
    return final_counts

# Lire les données depuis Cassandra
def read_data_from_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect(CASSANDRA_KEYSPACE)
    rows = session.execute(f"SELECT text FROM {CASSANDRA_TABLE}")
    data = [row.text for row in rows]
    session.shutdown()
    cluster.shutdown()
    return data

if __name__ == "__main__":
    n = 2  # Taille du n-gram

    # Lire les données depuis Cassandra
    dataset = read_data_from_cassandra()

    # Créer un pool de processus pour le traitement MapReduce
    pool = multiprocessing.Pool()

    # Effectuer le mapping
    mapped_results = pool.map(lambda doc: mapper(doc, n), dataset)

    # Effectuer la réduction
    reduced_result = reducer(mapped_results)

    # Afficher les résultats
    for ngram, count in reduced_result.items():
        print(f"{ngram}: {count}")
