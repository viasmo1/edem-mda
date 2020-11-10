# Kafka - Lab 0 

## Objetivos

 1) Ejecutar Zookeeper + Kafka
 2) Chequear estado
 3) Crear un topic

### Requisitos

 * Docker para Windows o Mac o Linux
 * Docker Compose 

## Run (Ejecutar)
Escenario simple: 1 zookeeper + 1 Kafka broker.

Inicie el contenedor ZooKeeper y Kafka.

```sh
$ docker-compose up -d
```

Status: 

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab0_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab0_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```

### Zookeeper 

Consulte los logs de ZooKeeper para verificar que ZooKeeper esté en buen estado.

```sh
$ docker-compose logs zookeeper | grep -i binding
```

Ejemplo de salida: 

```sh
zookeeper    | [2020-02-18 15:49:28,229] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
```

### Broker 

Consulte los logs de Kafka para verificar que el corredor esté en buen estado.

```sh
$ docker-compose logs kafka | grep -i started
```

Ejemplo de salida: 

```sh
kafka_1      | [2020-02-18 16:05:21,153] INFO [SocketServer brokerId=1] Started 2 acceptor threads for data-plane (kafka.network.SocketServer)
kafka_1      | [2020-02-18 16:05:21,646] DEBUG [ReplicaStateMachine controllerId=1] Started replica state machine with initial state -> Map() (kafka.controller.ZkReplicaStateMachine)
kafka_1      | [2020-02-18 16:05:21,663] DEBUG [PartitionStateMachine controllerId=1] Started partition state machine with initial state -> Map() (kafka.controller.ZkPartitionStateMachine)
kafka_1      | [2020-02-18 16:05:21,715] INFO [SocketServer brokerId=1] Started data-plane processors for 2 acceptors (kafka.network.SocketServer)
kafka_1      | [2020-02-18 16:05:21,727] INFO [KafkaServer id=1] started (kafka.server.KafkaServer)
```

### Crear un Topic
Cree un topic Kakfa llamado `myTopic`, con una partición y una réplica.

```sh
$ docker-compose exec kafka kafka-topics --create --topic myTopic --partitions 1 --replication-factor 1 --if-not-exists --zookeeper host.docker.internal:2181
```

Ejemplo de salida: 

```sh
Created topic myTopic.
```

Consulte la información del Topic:

```sh
$ docker-compose exec kafka kafka-topics --describe --topic myTopic --zookeeper host.docker.internal:2181
```

Ejemplo de salida: 

```sh
Topic: myTopic  PartitionCount: 1       ReplicationFactor: 1    Configs:
        Topic: myTopic  Partition: 0    Leader: 1       Replicas: 1     Isr: 1
```

### Clean up (Limpiar)

Apagar Docker Compose

```sh
$ docker-compose down
```
