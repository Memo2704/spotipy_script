# Spotify Script

A script that returns differents features of spotify using Spotipy module.

## Getting Started

Follow these instructions in order to run the script without problems. 

### Prerequisites

What things you need to install the software and how to install them

```
git clone https://github.com/Memo2704/spotipy_script.git
cd /spotify_script
```
Install virtualenv if you don't have it. 

```
pip install virtualenv --user 
```

Create and activate the virtual environment and then install the required dependencies.
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Installing

The first thing you need to do is change the names of these files: 

```
.env.edit
database.env.edit
```
The first file has the environments variables required by the spotify web api in order to run with the correct 
credentials set. 
```
SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI
```
The second file has the variables names with its values, that will be used to create the database.
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```
In order to create the database run the following command inside the project folder.
```
docker-compose up
```
```
#!docker-compose.yml
version: '3'
services:
  database:
    image: "postgres"
    env_file:
      - database.env
    volumes:
      - database-data:/var/lib/postgresql2/data/
    ports:
      - 5432:5432 
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
volumes:
  database-data: # named volumes can be managed easier using docker-compose
```
The previous command will create two containers. One running the database and the other running adminer 
that will let you manage the database with no problems.

## Running the script.

To run the script you will need to run the following command inside the project folder.

```
python spotify_script.py 9ta1ql0tgpzhg5cwbz58z2yr9
```
The first time you run this command it will open the default browser you have. And it will redirect you to
the previously set SPOTIPY_REDIRECT_URI which is 'http://google.com' but it will have the authorization code required by
the script, you'll need to copy that and paste it in the terminal when prompted.

### Options inside script

After running the script it will prompt the user to select one option out of 4 (5 is exit).
The option that matters is option 4. This option will asks you to put one or more artists inside a list to later iterate
with that list getting the Id of each artist, returning 50 songs and saving them inside the previously set database. 
```
0 - See how many songs you have in your playlists?
1 - See your top tracks!
2 - See your top artists!
3 - See top tracks of any artist you want!
4 - Want to make a list of artists and save those songs for later? Pick me!
5 - Exit
Your choice: 4
>>> This choice is a bit different, nothing difficult tho, let me explain!
>>> I'm going to add all of the artists (and songs) you want, to a safe place!
>>> All you need to do is type one by one the name of the artists, and then I'll show 50 songs of those artists
>>> 'Yes' if you want to continue adding artists, 'No' if you are done.
Name of the artist: korn
Do you want to continue adding artists?  (y/N)  yes
Add other artist: slipknot
Do you want to continue adding artists?  (y/N)  no
>>> This is Korn
  0 Freak On a Leash
...
```

### Inside adminer

After you finish using the script, if you want to see songs added inside the db. 
Get inside your localhost at port 5432 and login with the credentials set in `docker-compose.yml` and `database.env.`

```
localhost:5432
```

## Built With

* [Python](https://www.python.org/) - The language used.
* [Spotipy](https://spotipy.readthedocs.io/en/2.9.0/#) - Python library for the Spotify Web API
* [Docker](https://www.docker.com/get-started) - open platform for developing, shipping, and running applications.


## Authors

* **Tony Arteaga** - *Challenge work* 
