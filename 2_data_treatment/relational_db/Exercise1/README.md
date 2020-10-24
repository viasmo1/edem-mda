# Creating a Data Model

## Introduction

In this exercise we will be creating a Data Model for the use case below.

## Setup

1. Enter on http://www.draw.io 
2. Chose the storage location (if not selected already). For example Google Drive.
3. Choose to "Create a New Diagram"
4. Select "Blank Diagram", enter the diagram name, and the root folder you want to use. 
5. Authorize the app in Google (if requested)
6. Once in the canvas, click on "More shapes" and add "Entity Relation". Feel free to uncheck the rest in order to avoid confusion.
7. Implement an entity relationship of following the below case.

As a reference, you might find useful the following guide:

https://drawio-app.com/entity-relationship-diagrams-with-draw-io/

It includes a sample ER diagram which might be helpful when creating your first diagram. Just click on "Open this diagram in draw.io".

## Case

A TV company wishes to develop a database to store data about the TV series that the company produces. The data includes information about actors who play in the series, and directors who direct the episodes of the series. Actors and directors are employed by the company. A TV series are divided into episodes. Each episode may be transmitted at several occasions. An actor is hired to participate in a series, but may participate in many series. Each episode of a series is directed by one of the directors, but different episodes may be directed by different directors.

## Tips

* Feel free to go for the conceptual model or the logical model, or even both! Although we recommend de logical model as it is closer to what we will implement in the exercise 2, and it can be simplified by "minimizing" the entities.
