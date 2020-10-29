# SQL Exercise

Please follow this instructions to create your own database in local:

1) Git pull my repository

![Pushing and Pulling - GitKraken Documentation](https://support.gitkraken.com/img/documentation/repositories/pushing-pulling/set-default.png)

2) Navigate to the path where the docker compose file is:

`Mode                LastWriteTime         Length Name`

----                -------------         ------ ----
`d-----       26/10/2020     17:22                dvdrental`
`-a----       14/10/2019     18:26          10598 ALUMNOS.csv`
`-a----       14/10/2019      9:48          23923 ALUMNOS.sql`
`-a----       14/10/2019     18:28           3023 ALU_MASTER.csv`
`-a----       14/10/2019      9:49          19197 ALU_MASTER.sql`
`-a----       26/10/2020     16:54           1215 docker-compose.yml`
`-a----       14/10/2019     18:29           1053 MASTERS.csv`
`-a----       14/10/2019      9:32           5398 MASTERS.sql`

3) Once in this folder run the following command:

`docker-compose up`

4) Navigate to localhost:1234  (admin / password)

5) Create a new server with this config:

*Host: db*

*Port: 5432*

*Username: gft*

*Password:1234*

6) Create a database with name: **dvdrental**

7) Database Restore from File **dvdrental/dvdrental.tar**