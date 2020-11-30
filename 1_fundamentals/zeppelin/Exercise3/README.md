# Session ING-005 

During this session we will perform a real analysis using a dataset.

For this session, we will not need the rest of components so feel free to start a new container or re-use the one from the compose.

Before we start please perform the following actions in order to work them propertly.

```bash
docker exec -it zeppelin /bin/bash
```

Once inside the container perform the following commands:

```
apt-get update
apt-get upgrade
apt install python3-pip
pip3 install --upgrade pip
pip3 install seaborn
pip3 install pandas
```

If you have not reused the one from the composer, ensure that in the folder you run docker compose you find the following structure:

```
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       27/02/2020     17:14                data
d-----       18/02/2020     16:17                shared
d-----       20/02/2020      8:21                zeppelin
```

where inside data you have the following CSV:

```
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       12/02/2020     17:19        8945067 fifa_players.csv
```

Now you can navigate to your Zeppelin and import the notebook present in this exercise.