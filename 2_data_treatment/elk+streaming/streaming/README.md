# Stream Processing

## Spark Streaming Demo

Main purpose of this exercise is to execute an Streaming word count application over a tumbling window and see the result. For doing that, we will execute this [class](https://github.com/apache/spark/blob/master/examples/src/main/scala/org/apache/spark/examples/streaming/NetworkWordCount.scala). Those are the steps that you need to follow:

* Launch a spark master docker container on a command interface:

    ```sh
    docker run --name spark-master -h spark-master -e ENABLE_INIT_DAEMON=false -d bde2020/spark-master:2.4.5-hadoop2.7
    ```

* Check the container is running:

    ```sh
    docker ps
    ```

* On same console init a ssh session on spark-master container:

    ```sh
    docker exec -it spark-master bash
    ```
    
* Init a netcat server:

    ```sh
    nc -lkp 9999
    ```

* Open another command interface and connect to the same master container:

    ```sh
    docker exec -it spark-master bash
    ```

* Now launch an Spark streaming job:

    ```sh
    ./spark/bin/run-example streaming.NetworkWordCount localhost 9999
    ```

* Now start writing lines on the netcat console

* See the output on Spark Submit console. What do you think is the window used and the functionality implemented? *Fixed window*
