# ETL Exercise

## Load the database created in the SQL session

1) Navigate to the path where the sql docker compose file is

2) Run the following command:

`docker-compose up -d`

## Exercise 1

<img src="Exercises/Ex1.png" width="400px">

### Solution

#### Read csv file: ALUMNOS.csv

<img src="Solutions/Sol1_read_csv.png" width="250"/>

#### Select and configure tFileOutputJson component

<img src="Solutions/Sol1_outputJSON.png" width="400"/>

#### Final job

<img src="Solutions/Sol1.png" width="400"/>

#### Output JSON: Sol1.json

[Sol1.json](Solutions/Sol1.json)

## Exercise 2

<img src="Exercises/Ex2.png" width="250px">

### Solution

#### Read csv file: Ex2.csv

<img src="Solutions/Sol1_read_csv.png" width="250"/>

#### Select and configure tReplace component

<img src="Solutions/Sol2_tReplace.png" width="450"/>

#### Select and configure tFileOutputJson component

<img src="Solutions/Sol2_outputJSON.png" width="400"/>

#### Final job

<img src="Solutions/Sol2.png" width="400"/>

#### Output JSON: Sol2.json

[Sol2.json](Solutions/Sol2.json)

## Exercise 3

<img src="Exercises/Ex3.png" width="250px">

### Solution

#### Connect to postgres db dvdrental

https://youtu.be/3tF_6JGIsuA

Add connection

<img src="Solutions/Sol3_db_connection.png" width="250"/>

Configure connection

<img src="Solutions/Sol3_db_connection_2.png" width="450"/>

Add schemas

<img src="Solutions/Sol3_db_connection_3.png" width="350"/>

#### Select actor table

https://youtu.be/aQlD-KURSlc

<img src="Solutions/Sol3_actor.png" width="400"/>

#### Select and configure tFileOutputJson component

<img src="Solutions/Sol3_outputJSON.png" width="400"/>

#### Final job

<img src="Solutions/Sol3.png" width="300"/>

#### Output JSON: Sol3.json

[Sol3.json](Solutions/Sol3.json)

## Exercise 4

<img src="Exercises/Ex4.png" width="400px">

### Solution

https://youtu.be/nKF2fxJYfc4

#### Select film table

<img src="Solutions/Sol4_film.png" width="400"/>

#### Add and configure tAggregateRow

<img src="Solutions/Sol4_aggregateRow_1.png" width="400"/>

<img src="Solutions/Sol4_aggregateRow_2.png" width="400"/>

#### Select and configure tFileOutputJson component

<img src="Solutions/Sol4_outputJSON.png" width="400"/>

#### Final job

<img src="Solutions/Sol4.png" width="400"/>

#### Output JSON: Sol4.json

[Sol4.json](Solutions/Sol4.json)

## Exercise 5

<img src="Exercises/Ex5.png" width="450px">

### Solution

https://youtu.be/RsZqWlDTHmY

#### Final job

<img src="Solutions/Sol5.png" width="400"/>

#### Output JSON: Sol5.json

[Sol5.json](Solutions/sol5.json)

## Exercise 6

<img src="Exercises/Ex6.png" width="500px">

### Solution

https://youtu.be/vqox4KDe_0I

#### Final job

<img src="Solutions/Sol6.png" width="400"/>

#### Output JSON: Sol6.json

[Sol6.json](Solutions/Sol6.json)

## Exercise 7

<img src="Exercises/Ex7.png" width="500px">

### Solution

https://youtu.be/RsZqWlDTHmY

#### Final job

<img src="Solutions/Sol7.png" width="400"/>

#### Output JSON: Sol7.json

[Sol7.json](Solutions/Sol7.json)

## Exercise 8

<img src="Exercises/Ex8.png" width="500px">

### Solution

https://youtu.be/RsZqWlDTHmY

#### Final job

<img src="Solutions/Sol8.png" width="400"/>

#### Output JSON: Sol8.json

[Sol8.json](Solutions/Sol8.json)