# Projet MapReduce avec Amazon Reviews Dataset

Ce projet implémente un pipeline de traitement des données utilisant plusieurs technologies Big Data pour analyser les avis Amazon. Le pipeline inclut les étapes de téléchargement des données, de chargement dans une base de données NoSQL (Cassandra), et de traitement des données avec une approche MapReduce.

## Table des Matières

1. [Introduction](#introduction)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Téléchargement et Préparation des Données](#téléchargement-et-préparation-des-données)
5. [Chargement des Données dans Cassandra](#chargement-des-données-dans-cassandra)
6. [Traitement MapReduce](#traitement-mapreduce)
7. [Résultats](#résultats)
8. [Screenshots](#screenshots)
9. [Conclusion](#conclusion)

## Introduction

Ce projet est conçu pour traiter les avis des utilisateurs d'Amazon en utilisant un pipeline de traitement de données Big Data. Nous avons étudié et utilisé plusieurs technologies dont Kafka, Hadoop, Elasticsearch, Spark, Apache Cassandra, et MongoDB.

## Prérequis

- Java 8 ou Java 11 (OpenJDK ou Oracle JDK)
- Python 3.6+
- Cassandra
- Virtualenv
- Kaggle API

## Installation

### Étape 1: Installation de Java

```bash
sudo apt update
sudo apt install openjdk-11-jdk
java -version
```

### Etape 2 : Installation de Cassandra
```bash
wget https://downloads.apache.org/cassandra/4.0.7/apache-cassandra-4.0.7-bin.tar.gz
tar -xvzf apache-cassandra-4.0.7-bin.tar.gz
sudo mv apache-cassandra-4.0.7 /opt/cassandra
echo 'export CASSANDRA_HOME=/opt/cassandra' >> ~/.bashrc
echo 'export PATH=$PATH=$CASSANDRA_HOME/bin' >> ~/.bashrc
source ~/.bashrc
cassandra -f
```
### Etape 3 :  Installation de Python et Virtualenv
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install virtualenv
```
### Etape 4 :  Création de l'environnement virtuel
```bash
mkdir amazon_reviews_project
cd amazon_reviews_project
virtualenv venv
source venv/bin/activate
```

### Etape 5 :  Installation des dépendances Python
```bash
pip install requests cassandra-driver pyspark Flask scikit-learn pymongo kaggle
```

### Etape 6 : Téléchargement et Préparation des Données
Téléchargement du Dataset Amazon Reviews
Script download_dataset.py

Ce script télécharge le dataset depuis Kaggle en utilisant l'API Kaggle.

Path : download_dataset.py
Exécution du script de téléchargement

```
python download_dataset.py
```

### ETape 7 : Chargement des Données dans Cassandra
Script load_to_cassandra.py

Ce script charge le dataset téléchargé dans une table Cassandra.

Path : load_to_cassandra.py
Exécution du script de chargement

```
python load_to_cassandra.py
```

### Etape 8 : Traitement MapReduce
Script map_reduce.py

Ce script lit les données depuis Cassandra et effectue un traitement MapReduce.

Path : map_reduce.py
Exécution du script MapReduce
```
python map_reduce.py
```

### Screenshots : 

![Clef de Cassandra]("key cassandra.png")
![Dependances.png]("dependances.png")