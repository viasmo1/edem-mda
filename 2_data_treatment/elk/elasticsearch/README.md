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


## Exercises

**Objective**: you will see how quickly and easily the Elastic Stack can be used to search a dataset. You will startup Elasticsearch and Kibana, then run queries from Kibana to search an indexed dataset.

*Note*: The datasets we are going to use are on the following folder: ../docker/data

* Launch docker compose with full ELK stack
```
cd ../docker
docker-compose up -d
```

* Open your Web browser and go to http://localhost:9200.

**Response:**

```json
{
  "name" : "elasticsearch",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "SHsA7iQDQYKvnHnYzZvMcQ",
  "version" : {
    "number" : "7.3.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "de777fa",
    "build_date" : "2019-07-24T18:30:11.767338Z",
    "build_snapshot" : false,
    "lucene_version" : "8.1.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

* Based on previous output:
    * What is the version of Elasticsearch instance? ***7.3.0***
    * What is the name of your node? ***elasticsearch***
    * What is the name of your cluster? ***docker-cluster***

* Analyse the dataset we are going to use (data/products). The dataset you are going to be using is a collection of products sold in stores. The fields in the dataset consist of:
    * grp_id: a unique ID for each row
    * upc12: a 12-digit string containing the Universal Product Code
    * brandName: the name of the company that makes the product
    * productName: the name of the product
    * customerRating: an integer value between 1 and 5, where 5 is the highest rating
    * price: a float value representing the price of the product
    * quantitySold: an integer value representing the number of units

Small sample of what the data looks like:
```
20,204040000000,Usda Produce,Plums Black,3,1.39,68603
21,753950001954,Doctor's Best,Doctor's Best Best Curcumin C3 Complex 1000mg Tablets - 120 Ct,2,1.75,651857
22,016000288829,Betty Crocker,Betty Crocker Twin Pack Real Potatoes Scalloped 2 Pouches For 2 Meals - 2 Pk,2,4.22,527899
23,070670009658,Reese,Reese Mandarin Oranges Segments In Light Syrup,2,3.73,104348
24,688267084225,Smart Living,Smart Living Charcoal Lighter Fluid,5,3.20,637769
25,044100117428,Hood,Hood Latte Iced Coffee Drink Vanilla Latte,5,5.99,166777
```

* The products dataset was indexed already into your Elasticsearch instance. Go to http://localhost:9200/_cat/indices?v. Your products index should appear in the list of indices. (Notice the size may vary, but it should contain 110,435 documents):

<img src="../img/indices.png" size=500px>

* To view the products data, use the Search API with the following URL: http://localhost:9200/products/_search. You should see 10 products (10 is the default search size). The products displayed will likely vary from the output below, but notice the output is not very pretty:

<img src="../img/products.png" size=500px>

* Change the URL to include the pretty argument: http://localhost:9200/products/_search?pretty. The output should now look much nicer:

<img src="../img/products_pretty.png" size=500px>

* Based on the output of previous search:
    * How many documents were indexed? ***At least 10k. The relation "gte" tells us that the number of documents are Greater or Equal than 10k***
    * What is the _type of each document? ***"product"***


### Kibana

Next, you are going to use Kibana. To verify Kibana is running, open your Web browser and go to http://localhost:5601. The Kibana application should appear.

* Click on the Dev Tools button (left side tool icon) in the side navigation pane to open the Console application.

    * Notice there is a match_all query already written in the Console. Go ahead and run it by clicking the green "play" button that appears to the right of the command, or using the Ctrl/Cmd + Enter keyboard shortcut. This search hits all documents in all indexes of your cluster. Notice the output is similar to the output you saw a few minutes ago, but displayed nicely in the Console screen.

* Now let's search for products. Enter the following query into the Console, just below your first command. It answers the question "Which products have peanut or butter in the product name?"

```json
GET products/_search
{
  "size": 25,
  "query": {
	"match": {
  	"productName": "peanut butter"
	}
  }
}
```

**Response**

[full json](prods_name_peanut_butter.json)

```json
{
  "took" : 322,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2011,
      "relation" : "eq"
    },
    "max_score" : 11.242394,
    "hits" : [
      {
        "_index" : "products",
        "_type" : "product",
        "_id" : "108162",
        "_score" : 11.242394,
        "_source" : {
          "upc12" : "074333470441",
          "grp_id" : "108162",
          "customerRating" : 3,
          "quantitySold" : 655728,
          "price" : 19.36,
          "productName" : "Peanut Butter Creamy",
          "type" : "csv",
          "brandName" : "Arrowhead Mills"
        }
      }
      ...
```

* Based on the results of your previous search:

    * How many products in the dataset match "peanut butter" in the product name? ***2011*** 
    * What was the max_score of the results? ***11.242394***
    * Would you say that your top results were relevant to "peanut butter"? ***Of course. All the results contain at least one of those words in the name***

* Change the term "peanut butter" to "Peanut Butter" and run the query again. What is different in the results, if anything? ***The response time of the query is much lower. BUT, this is because the former result is in caché. Elastic is NOT case sensitive***

* Run a search for "kasmati rice" in the "productName", then answer the following questions:
    * How many hits are there? ***1618***
    * What was the _score of the top hit? ***19.586052***
    * View the scores of the next few hits. Why do you think the top hit had a much higher score than all the other hits? ***The name of the top hit contains both, kasmati and rice in the name. The following results don't***

* Compare the following search to the previous ones you executed. Notice the field being searched on is now customerRating. Run the following query, which answers the query: "Find all products with a customer rating of 4".

    ```json
    GET products/_search
    {
    "query": {
        "match" : {
        "customerRating" : 4
        }
    }
    }
    ```

**Response**

[full json](prods_rating_4.json)

*Notice the score for each hit is simply 1. Why do you think all matching documents have the same score? ***All the results have a rating of exactly 4****

* Write a query that finds all products whose price field is exactly 10.00. You should get 44 hits.

```json
GET products/_search
{
  "query": {
	"match" : {
  	"price" : 10.00
	}
  }
}
```

* Response

[full json](prods_price_10.json)