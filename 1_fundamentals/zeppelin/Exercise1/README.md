# Get familiar with Notebooks: Zeppelin

## Author

[Pedro Nieto](https://github.com/a10pepo)

[Original Repo](https://github.com/a10pepo/edem2021/tree/master/Sesiones/zeppelin)

Modified and solved by [me](https://github.com/viasmo1)

### Create Zeppelin container

* Open Terminal

* Go to the Exercise1 folder

* Run below command 
```bash
docker run -d -p 19999:8080 --rm --name zeppelin_1 apache/zeppelin:0.8.1
```

### Open your Zeppelin

* Run below command 
```bash
http://localhost:19999
```
* Once opened, import the notebook present in your folder:

![Zeppelin1](https://github.com/viasmo1/edem-mda/tree/master/1_fundamentals/zeppelin/images/zeppelin_1.png)

![Zeppelin2](https://github.com/viasmo1/edem-mda/tree/master/1_fundamentals/zeppelin/images/zeppelin_2.png)

Now we will see different things we can configure inside a notebook what can we configure to adapt to our needs.

# Exercise 1: 

Create a notebook with the following structure:

![Zeppelin3](https://github.com/viasmo1/edem-mda/tree/master/1_fundamentals/zeppelin/images/zeppelin_3.png)