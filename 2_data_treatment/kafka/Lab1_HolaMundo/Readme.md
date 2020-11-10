# Kafka - Lab 1 

## Objetivos

 1) Ejecutar Zookeeper + Kafka
 2) Producir y leer mensajes desde la línea de comando
 3) Producir y leer mensajes desde Java
 4) Producir y leer mensajes desde línea de comando y/o Java

### Requisitos

 * Docker para Windows, Mac o Linux
 * Docker Compose 

## Run
Escenario simple: 1 zookeeper + 1 Kafka broker.

Inicie el contenedor ZooKeeper y Kafka.

```sh
$ docker-compose up -d
```

Estado: 

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab1_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab1_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```

### Productor Kafka de linea de comando

Ejecutar el productor de línea de comandos:

```sh
$ docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
>hi
>dlp
>

```

Leer el contenido del topic:

```sh
$ docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
hi
dlp
```

### Ejemplo de Java

El ejemplo es un proyecto de Maven. Opcional: Como ejercicio avanzado puede importar el proyecto como proyecto Maven con su IDE (IntelliJ IDE o Eclipse).

* Productor: El productor generará 100 mensajes y los enviará a `myTopic`. 
* Consumidor: consumir y registrar mensajes de `myTopic`.  

```sh
$ cd kafka-example 
```

Compilar projecto/código Java: 

```sh
$ mvn clean compile
```

###  Consumidor Java

Ejecutar el consumidor

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.Consumer"
```
El consumidor escuchará y registrará nuevos mensajes.

#### Ejercicios 

* ¿Cómo puede la lista de consumidores iniciar todos los mensajes del tema?  Pista: *auto.offset.reset*
 
###  Productor

Ejecuta el productor

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.Producer"
``` 

#### Ejercicios 

Pruebe otras combinaciones: produzca mensajes desde la consola y consumalos desde Java o viceversa. 

### Clean up

Apagar Docker Compose

```sh
$ docker-compose down
```
