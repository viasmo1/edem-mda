# Data types, sources and frequency

## Author

[Roberto López](https://github.com/rlopezherrero/)

[Original Repo](https://github.com/rlopezherrero/GFT-EDEM-MasterData/tree/master/CapturaRecogida)

## Exercise 1
In this exercise you will navigate over several example XMLs and you will create one as an example.

- Access to this URL and see how it is structured an XML → https://www.w3schools.com/xml/plant_catalog.xml 
    - What contains this catalog? **Plant catalog**
    - How many properties has the main element of the catalog? **6**

- Access to this URL to load another XML → https://www.w3schools.com/xml/note_error.xml
    - What happens when you try to load it? **Gives an error**

- Go to https://codebeautify.org/xmlviewer and load previous xml url. 
    - Could you identify what is the error and fix it? **Error closing tag line 4**


## Exercise 2
Let’s create an XML file:
- Using this table description create an XML file manually:

| Id | Car Model | Color | Year | Owner Name | Owner Address | Owner Phone |
| -- | -- | -- | -- | -- | -- | -- |
| 1111CXY | Opel | Red | 2014 | Jacinto Rodriguez | Av. Taronjers 10 | 777777777 |
| 0000DDD | BMW | Blue | 2010 | Alicia García | C/ Colon 9 | 111111111 |


**XML**

```shell
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
    <car num="1">
        <id>1111CXY</id>
        <model>Opel</model>
        <color>Red</color>
        <year>2014</year>
        <ownerName>Jacinto Rodriguez</ownerName>
        <ownerAdress>Av. Taronjers 10</ownerAdress>
        <ownerPhone>777777777</ownerPhone>
    </car>
    <car num="2">
        <id>0000DDD</id>
        <model>BMW</model>
        <color>Blue</color>
        <year>2010</year>
        <ownerName>Alicia García</ownerName>
        <ownerAdress>C/ Colon 9</ownerAdress>
        <ownerPhone>111111111</ownerPhone>
    </car>
    <car num="3">
        <id>1111VAM</id>
        <model>Ferrari</model>
        <color>Red</color>
        <year>2020</year>
        <ownerName>Vicent Asensio Molina</ownerName>
        <ownerAdress>C/ Colon 9</ownerAdress>
        <ownerPhone>111111111</ownerPhone>
    </car>
</catalog>
```

- Go to https://codebeautify.org/xmlviewer and load this XML to test that is well formed.
- Have you created nested elements? **Yes**


## Exercise 3
JSON files management, creating one as an example and accessing to the data:
- Take a look to an example Kaggle CSV file of sales https://www.kaggle.com/kyanyoga/sample-sales-data/version/1#sales_data_sample.csv
- See the content and Download the file
- Go to https://codebeautify.org/jsonviewer, and create a JSON of 2 first records of the file

**JSON**

```shell
{
  "order": [
    {
      "orderNumber": 10107,
      "quantityOrder": 30,
      "priceEach": 95.7,
      "orderLineNumber": 2,
      "sales": 2871,
      "orderDate": "2/24/2003 0:00",
      "status": "Shipped",
      "QTR_ID": 1,
      "MONTH_ID": 2,
      "YEAR_ID": 2003
    },
    {
      "orderNumber": 10121,
      "quantityOrder": 34,
      "priceEach": 81.35,
      "orderLineNumber": 5,
      "sales": 2765.9,
      "orderDate": "5/7/2003 0:00",
      "status": "Shipped",
      "QTR_ID": 2,
      "MONTH_ID": 5,
      "YEAR_ID": 2003
    }
    ]
}
```
- Now parse it on Python:
    - Open Jupyther Notebook:
        - Go to git downloaded repo (https://github.com/rlopezherrero/GFT-EDEM-MasterData/tree/master/CapturaRecogida)
        - Run ‘docker-compose up -d’ to launch Jupyter Notebook        
        - Open http://localhost:8888
        - Logon using password ‘edem’

- Load EDEMCRExercise3.ipynb available on downloaded Git repository (https://github.com/rlopezherrero/GFT-EDEM-MasterData/tree/master/CapturaRecogida)

- Follow the instructions
    - Solved Notebook: [Exercise3_solved.ipynb](EDEMCRExercise3_solved.ipynb)


## Exercise 4
Let’s play downloading and uploading files using SFTP protocol.
- If you don’t have it, download and install an SFTP Client
    - Windows → https://winscp.net/eng/docs/lang:es
    - Linux → https://filezilla-project.org/download.php?platform=linux64
    - Mac Os X → https://filezilla-project.org/download.php?platform=osx

- On login screen login on remote server
    - Host → 34.66.154.152
    - User → edemExercise3
    - Password → edemExercise3
    - Port → 22 (Filezilla)
 
- Now you have started a remote connection and can access to the file system of this machine.  You see home directory of edemExercise3 user.

 
- Download SFTPTest.txt file to your local machine (drag from right and drop on left).
- Edit txt file and add a line with a comment of our preference. 
- Rename the txt file adding your name to the file name (ex. SFTPTestRoberto.txt) 
- Enter inside Upload folder of the remote machine, and create a directory with your name. 
- Upload inside this created directory the file you created. 


## Exercise 5
This exercise you will access to an API Restful Service to query posts and comments of a Web Service
- Using web browser GET the posts that are available here → https://jsonplaceholder.typicode.com/posts 

- What is the format of the output? **JSON**

- How you would get post 1? **https://jsonplaceholder.typicode.com/posts/1**

- This application has also comments, how you will get them? **https://jsonplaceholder.typicode.com/comments**

- How you would get all the comments for post 1? 
**https://jsonplaceholder.typicode.com/comments?postId=1**

- Now let’s do with Python:
    - Open Jupyter Notebook → https://jupyter.org/try
    - Upload EDEMCRExercise5 available on downloaded git repository ( available on downloaded Git repository (https://github.com/rlopezherrero/GFT-EDEM-MasterData/tree/master/CapturaRecogida)

    - Follow the instructions on the Notebook
        -  Solved Notebook: [Exercise5_solved.ipynb](EDEMCRExercise5_solved.ipynb)


## Exercise 6
On this exercise you will execute a python job to upload a file to  a remote server via SFTP. Here you have the api documentation that you can use ( https://pysftp.readthedocs.io/en/stable/pysftp.html)
- Use jupyther Notebook , also used on exercise 3 ( https://jupyter.org/try)
- Download template available on GIT ---> https://github.com/rlopezherrero/GFT-EDEM-MasterData/blob/master/CapturaRecogida/EDEMCRExercise6.ipynb
- Create a local text file with your name.
- Following the template develop a file upload using following connection:
    - Host → 34.66.154.152
    - User → edemExercise3
    - Password → edemExercise3
    - Folder → Upload/YourName (folder you created on exercise 3)
-  Solved Notebook: [Exercise6_solved.ipynb](EDEMCRExercise6_solved.ipynb)






