# Implementing the Data Model

## Introduction

In this exercise we will be creating the database based on the previous exercise. For this purpose, we will use the popular MySQL database.
We have also included a UI to easily browse it, but we highly recommend to do the exercise using the command line.

## Setup

Let first launch the database and the UI. In the root folder run the following:

```shell
docker-compose up -d
```

Now, connect to the database:

```shell
# Modify records in the database via MySQL client
docker-compose exec db bash -c 'mysql -u root -pexample'
```

And perform some basic queries in the MySQL screen:

```shell
# Switch to the "mysql" database (internal database)
mysql> use mysql;

# List the tables
mysql> show tables;

# Show the sturcture of a table
mysql> describe user;

# Query the "user" table
mysql> SELECT host, user FROM user;
```

Now take a look at the same using the UI: http://localhost:8080/

## Exercise

Now it is your turn. You will need to create the tables you defined in the Entity Relationship model for Exercise 1.

But first, let's create a separate database for it:

```shell
# Create the new database
mysql> create database edem;

# Switch to the new database
mysql> use edem;

# Confirm there are no tables
mysql> show tables;
```

Just as an example, let's create a sample table:

```shell
# Create the new database
mysql> CREATE TABLE PEN (
	NAME VARCHAR (15) PRIMARY KEY, 
	TYPE VARCHAR (10), 
	PEN_COLOR VARCHAR (15),
	INK_COLOR VARCHAR (15),
	ORIENTATION VARCHAR (15),
	WEIGHT DECIMAL (3, 2),
	EASE_OF_USE BOOLEAN
);

# Confirm the table was created
mysql> show tables;

# Show the sctructure
mysql> describe PEN;

# Query the table 
mysql> select * from PEN;
```

Now, **create the tables in your Data Model**.

### Tips

* Create the tables in a TXT file first, and the run them one by one in the command line
* Beware of the execution order since there are dependencies due to Foreign Keys
* WARNING: table names are case sensitive!!

## Reference

* MySQL Documentation: https://dev.mysql.com/doc/refman/8.0/en/
* MySQL (Creating a table): https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html
* MySQL (Data Types): https://dev.mysql.com/doc/refman/8.0/en/data-types.html

