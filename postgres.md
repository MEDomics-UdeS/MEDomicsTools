# MEDomicsTools PostgreSQL Coding Standard

This document presents the PostgreSQL coding standard of the MEDomicsTools team.

## Table of Contents
- [MEDomicsUdeS PostgreSQL Coding Standard](#medomicsudes-postgresql-coding-standard)
  * [Table of Contents](#table-of-contents)
  * [Changelog](#changelog)
  * [Contributors](#contributors)
  * [To-Do](#to-do)
  * [PgAdmin](#pgadmin)
    + [R000 - Recommended Software](#r000---recommended-software)
    + [R001 - Server creation and database connection](#r001---server-creation-and-database-connection)
    + [R002 - Database creation](#r002---database-creation)
    + [R003 - User creation and modification](#r003---user-creation-and-modification)
    + [R004 - Real databases](#r004---real-databases)
  * [PostgreSQL](#postgresql)
  * [Python](#python)

NOTES:

- To update the Table of Contents, use: https://ecotrust-canada.github.io/markdown-toc/
- Section headers cannot contain special characters other than -, otherwise the TOC hyperlinks will not work

## Changelog

Revision | Date       | Description |
---------| -----------| ----------- |
B        | 2022-01-27 | Python      |
A        | 2021-11-18 | Creation    |

## Contributors

- [Olivier Lefebvre](https://github.com/Olivier998)

## To-Do

- [X] Table of contents
- [X] Server creation
- [ ] Database creation : ajout d'un exemple jouet
- [X] User creation and modification
- [ ] PostgreSQL section : queries et autres
- [ ] Résumé de ce [site](https://towardsdatascience.com/10-essential-psql-commands-for-data-engineers-c1ea42279160)
- [X] Python : Commandes pratiques et interaction entre Python et postgresql avec exemple jouet : Nic
- [ ] MIMIC: Add concepts tabs creation : Oli
- [ ] MIMIC and eICU: add table description : Oli
- [ ] Add table creation (And file to create the sapsii-24h tab) : Oli
- [ ] Linux user creation?  Peut-être juste en faire mention
- [ ] Faire une database jouet avec user jouet pour pratiquer les opérations : Nic?

## PgAdmin
### R000 - Recommended Software

Operating System:
- Ubuntu: https://ubuntu.com/

PostgreSQL Installation:
- postgres: [Installation](https://www.postgresqltutorial.com/install-postgresql/)

IDE:
- PgAdmin: [PgAdmin 4](https://www.pgadmin.org/download/)


### R001 - Server creation and database connection
Follow these steps to create a PostgreSQL server to access databases.

#### 1. Install PgAdmin and postgreSQL on your local computer.
To install PgAdmin and postgreSQL, see [R000 - Recommended Software](#r000---recommended-software).

#### 2. Connect to UDS VPN with Cisco AnyConnect.
If it’s the first time, follow the instructions at [UDS Cisco AnyConnect.](https://www.usherbrooke.ca/services-informatiques/repertoire/reseaux/rpv/guide-dutilisation-du-rpv/) ​

#### 3. Create a SSH tunnel to the server.
From your local computer, in the terminal, type: "ssh -f -L 5437:localhost:5432 usernameLX@10.44.86.27 -N".
Enter the password matching with your CIP (The same previously used with Cisco AnyConnect)

Notes :
 - 5437 stands for the local port to connect to the external localhost:5432 on the server.

 - usernameLX is your username (CIP), such as: test1234

#### 4. Create a server
Open PgAdmin. Right click on Servers then go to Create -> Server…​

- In the "General" tab:
  - Enter the name of your choice in the "Name" section.

- In the "Connection" tab:
  - Enter "localhost" in the Hostname/address section.
  - Enter "5437" in the "Port" section (or previous local port chosen at step 3.)
  - Enter your usernameSQL in the "Username" section (as test1234)
  - Enter your password for usernameSQL in the "Password" section (as test1234)
  - Click Save

Within your newly created server, you can now make queries from available Databases. You can try to execute step 4 with Username/password: test1234.

#### 5. Reconnecting to your server
Next time you want to access your server in pgAdmin:

- Repeat step 2 and step 3
- Open pgAdmin on your local computer
- Double-click on the newly created server icon and enter your password






### R002 - Database creation



### R003 - User creation and modification
To execute these steps, you must already have access to a postgres user account with create roles privileges.  
We create postgres users within PgAdmin, which is much easier.

#### 1. Connect to server
Connect to the desired server using a postgreSQL user account with create roles privileges (such as the postgres user). See section [Server creation](#r001---server-creation) for more details.

#### 2. Create user
Right-click on Login/Group Roles, and select Create/Login/Role

a. In the "General" tab: give the same user name as the Linuxs one on the system (e.g. vallieresm).

b. In the Definition tab: give the default password "medomics101".
           Be sure to send that username to the corresponding person by email.
           That person can later create his/her personal password using pgAdmin
	   (see the instructions file).

c. In the Privileges tab: allow "login". This will actually create a new user.
           Leave the other default parameters as is.

d. Click Save.

#### 3. Allow access to a schema (Skip to step 4 to allow access to all schemas in a specific database)
This step allows you to allow access to specific schemas in a database for the user. However, if you want to allow access to all schemas to the user, skip to step 4.

Navigate to the desired schema and right-click. Click on "Properties".

a. In the "Security" tab, click on "+" in the top-right corner

b. Add the corresponding username under "Grantee".

c. Check the "Usage" box (only) under "Privileges".

d. Click Save

#### 4. Allow access to all schemas in a specific database
Skip this step if you did step 3. If the schemas in the database are not 'public' (i.e. 'PUBLIC' is not granted usage privileges in the security tab), step 4 will not work. You have two options:
- a) Repeat step 3 for every schemas in your database
- b) Repeat step 3 for every schemas in your database, but using username 'PUBLIC' under "Grantee" at step 3.b. You will then be able to do step 4.

Navigate to the desired database and right-click. Click on "Properties".

a. In the "Security" tab, click on "+" in the top-right corner

b. Add the corresponding username under "Grantee".

c. Check the "connect" box (only) under "Privileges".

d. Click Save

#### 5. Allow access to tables
Right-click again on the desired database. Click on "Grant Wizard".

a. Select all Object types, accordingly to steps 3 and 4, and click "Next"

b. Click on "+" in the top-right corner.

c. Add the corresponding username under	"Grantee".

d. Check the "SELECT" box (only) under "Privileges".

e. Click "Next" and "Finish".

#### 6. Alter user privileges
To alter user's privileges, repeat steps 3-5 and allow desired privileges.

#### Troubleshooting
If the user can not access specified schemas or databases (assuming you did step 5. correctly), the problem may come from step 3 or 4.
For a user to have access to schemas, these schemas and the databases must be accessible for the user.  
That is in the database "security" tab, 'PUBLIC' or user is granted connect privileges, AND in every schemas "security" tab,  
'PUBLIC' or user is granted usage privileges.


### R004 - Real databases


#### Mimic-IV
##### Database creation

To create the Mimic-IV database, follow these next steps:

- You will first need to download the Mimic data from [Physionet](https://mimic.mit.edu/).
- You then need to download the [Mimic-code](https://github.com/MIT-LCP/mimic-code/tree/main/mimic-iv).
- You then only have to follow the steps given on the [mimic project](https://github.com/MIT-LCP/mimic-code/tree/main/mimic-iv/buildmimic/postgres).

#### eICU
##### Database creation
To create the eICU database, follow these next steps:

- Download the [eICU data](https://eicu-crd.mit.edu/).
- Download the [eICU code](https://github.com/MIT-LCP/eicu-code).
- Follow the [building steps](https://github.com/MIT-LCP/eicu-code/tree/master/build-db/postgres).
- However, you may need to specify a user and a database name while creating the eICU database.
- To do so, add the following parameters to the creation queries:
  - DBUSER=postgresUser (the postgresUser must be able to create a database)
  - DBPASS=password  (The password of the postgresUser)
  - DBNAME=DBNAME  (The name that you want to use for the database)
- The creation queries will then be as:
  - make initialize DBUSER=user DBPASS=password DBNAME=eicu
  - make eicu-gz datadir=/data/dir DBUSER=user DBPASS=password DBNAME=eicu



## PostgreSQL

## Python
### R005 - Interaction with PostgreSQL using psycopg2 and pandas
- The psycopg2 library enables to create a *connection* object that handles communication with a PostgreSQL database.
- From the psycopg2 doc: "*the connections are thread safe and can be shared among many threads.*".
- The next code snippet is an example of a function that creates a *connection*:
````python
import psycopg2

def create_cursor(user: str,
                  password: str,
                  database: str,
                  host: str,
                  port: str):
  """
  Creates a connection to a database
  
  Args:
      user: username to access the database
      password: password linked to the user
      database: name of the database
      host: database host address
      port: connection port number
      
  Returns: connection
  """
  try:
    conn = psycopg2.connect(database=database,
                            user=user,
                            host=host,
                            password=password,
                            port=port)

  except psycopg2.Error as e:
    raise Exception(e.pgerror)

  return conn
````
- From a *connection*, you can create a *cursor* object that is provided with methods to send queries to the database and extract data.
- From the psycopg2 documentation: "*the cursors are not thread safe. A multithread application can create many cursors from the same connection and should use each cursor from a single thread.*".
- Using *cursors* as context managers ensure that they will be closed when the context is left:
````python
with conn.cursor() as curs:
    curs.execute('SELECT * FROM public."MY_TABLE"')
    
# the cursor is now closed
````
- In order to handle data after its extraction, it is recommended to store it in a pandas 'Dataframe' object.
- The next example shows how to extract the table *MY_TABLE* from the *public* schema of a database using the function defined above:
````python
import pandas as pd

conn = create_cursor(user='username',
                     password='mypassword',
                     database='mydatabase',
                     host='localhost',
                     port='5432')

with conn.cursor() as curs:

    # We execute the query
    curs.execute('SELECT * FROM public."MY_TABLE"')

    # We retrieve the column names and the data
    columns = [desc[0] for desc in curs.description]
    data = curs.fetchall()

    # We create a pandas dataframe
    df = pd.DataFrame(data=data,
                      columns=columns)
    
````
