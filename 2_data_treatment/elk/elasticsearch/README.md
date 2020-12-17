# Elasticsearch Stack

## Infrastructure Setup

In order to **launch** the required infrastructure you just have to go to the "docker" folder and run the following:

```
docker-compose up -d
```

## Nutrition Demo

On this demo we will play with a nutrition dataset that you can take a look on following link [Nutrition dataset](../docker/data/nutrition/nutrition.csv)

1. Now open a web browser and enter on [Kibana](http://localhost:5601). And we will create a dashboard with the folowing
* Total number of products of the dataset.
* Pie chart with top5 brands containing products.
* Table with top 5 calorie products.
* TagCloud with ingredients more common.

Here you can see a screenshoot 

![Screenshot](../img/demoScreenshot.png)


