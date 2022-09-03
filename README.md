## Send Money project
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [N.B.](#Remember)

## General info
This project is a simple application for user register, login and send money.
	
## Technologies
Project is created with:
* Flask version: 3.9
* Python version: 2.2
* MongoDB version: 6.0
* virtualenv version: 20.16
	
## Setup
To run this project, you have to install the packages according to the configuration file:

```
$ pip install -r requirements.txt
```

### Then you set the envirement vars on windows

```
$ set FLASK_APP=app.py
$ set MONGODB_URI="your_mongodb_uri"
```

if you run this project locally

```
$ set FLASK_DEBUG=True
```
Finally

```
$ flask run
```
### On linux
you just need to execute the script on run file

```
$ ./run
```
# N.B.
With Flask applications we need to deel with virtual envirement so you should activate it before any installation above

```
$ path_env_folder/Scripts/activate
```
