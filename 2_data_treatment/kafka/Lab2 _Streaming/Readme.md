# Kafka Streams Lab,

## Objetivos

 1) Ejecutar Zookeeper + Kafka
 2) Producir messages  
 3) Procesar mensajes con Kafka Streams DSL
 4) Salida de Resultados 

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
 
### Descripción del ejemplo

El ejemplo es un proyecto de Maven. Opcional: Como ejercicio avanzado puede importar el proyecto como proyecto Maven con su IDE.

* **Productor de frases de Shakespeare**: El productor generará 1000 mensajes de citas de Shakespeare, utilizando el [Faker API](https://github.com/DiUS/java-faker), and send them to the `quotes-input`. 

 Ejemplos de frases: 
  * `True is it that we have seen better days.`
  * `Can one desire too much of a good thing?.`

* **Word Count**: WordCount, usa la API Kakfa de alto nivel [KStream DSL](https://docs.confluent.io/current/streams/developer-guide/dsl-api.html), will compute a simple word occurrence histogram from input quotes. In this example, the input stream reads from a topic named "quotes-input", where the values of messages represent lines of text; and the histogram output is written to topic "streams-wordcount-output", where each record is an updated count of a single word

* **Resultados del Consumidor**: El consumidor mostrará los mensajes del topic "streams-wordcount-output".

Ejemplo: 

```sh
     | think | 625
     | he | 625
     | is | 1852
     | wise | 1249
```

### Ejecutando

```sh
$ cd kafka-streams-example 
```

Compilar código Java: 

```sh
$ mvn clean compile
```

###  Consumer

Ejecute el Consumidor:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.Consumer"
```
(En Windowds use doble comillado de esta forma => -D"exec.mainClass")
 
 ###  WordCount
 
 Ejecute el procesador: 
 
 ```sh
 $ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.WordCountConsumer"
 ``` 
 (En Windowds use doble comillado de esta forma => -D"exec.mainClass")


###  Productor

Ejecute el productor:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.Producer"
``` 
(En Windowds use doble comillado de esta forma => -D"exec.mainClass")


### Producir mensajes con la Consola
```sh
$ docker-compose exec kafka kafka-console-producer --topic quotes-input --broker-list localhost:9092
```
#### Ejercicios avanzados  

* Filtrar palabras - Ejemplo: contar solo palabras con una longitud> 3

* Filtrar resultados - Ejemplo: recuento> 10000


### Clean up

Apagar Docker Compose

```sh
$ docker-compose down
```


