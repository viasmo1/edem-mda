# EDEM - Master on Data Analytics - NOSQL databases with Cassandra

## Author

[Esteban Chiner](https://github.com/echiner)

[Original repo](https://github.com/echiner/edem-mda-nosql-cassandra)

Modified and solved by [me](https://github.com/viasmo1)


## Introduction

<img width="250" src="http://cassandra.apache.org/img/cassandra_logo.png">

In this section we will setup **[Apache Cassandra](http://cassandra.apache.org/)** and read/write data from it.

## Initial setup

Use the following command to start all the components:

```shell
docker-compose up -d
```

As you will see, looks like one is missing. It is the CQL Shell, which is launched interactively:

```shell
# Start the CQL container, which points to the Cassandra database
docker-compose run cqlsh

# In the CQL prompt, check the config
cqlsh> SELECT cluster_name, listen_address, release_version FROM system.local;
```

## Exercises

* [**Exercise 1**: Basic syntax](Exercises/Exercise1)
* [**Exercise 2**: Creating a Data Model](Exercises/Exercise2)
* [**Exercise 3**: Inserting and reading data](Exercises/Exercise3)
* [**Exercise 4**: Ingesting and analyzing data in real-time](Exercises/Exercise4)

## Understanding the components

This architecture will lauch the following components:

* **Apache Cassandra**: NOSQL columnar database
* **CQL Shell**: Command line interface for CQL (Cassandra Query Language)
* **Apache NiFi**: Web-based data ingestion tool
* **Apache Zeppelin**:  Web-based notebooks

This table includes all required details:

| Component | Ports | URL/Comments |
| ------------- | ------------- | ------------- |
| **Apache Cassandra** | 9042  | N/A  |
| **CQL Shell** | N/A  | N/A  |
| **Apache NiFi** | 8888  | http://localhost:8888/nifi  |
| **Apache Zeppelin** | 9999  | http://localhost:9999/  |

## Documentation

* http://cassandra.apache.org/doc/3.11/