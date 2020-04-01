# Connectercise
This repository is for the WAD2 Team Project.

Connectercise is a website in which users can connect with other users to do sport together. Users can add sports (which act like categories) and under each sport,  there can be various requests, which are also created by the users.

## Using this Repository
Since this repository uses a virtual environment with specific packages, it is essential to activate it specifically.

```
$ git clone https://github.com/ineshbose/connectercise_project
$ cd connectercise_project
```

### Virtual Environment
If you haven't already created a virtual environment, you can do using using Anaconda.

```
$ conda create -n connectercise python=3.8.0
$ conda activate connectercise
```

### Installing packages
A `requirements.txt` file mentions all the packages along with their versions used for this project. You can install them using:

```
$ pip install -r requirements.txt
```

### Running the App
The main Python file is `manage.py`. It is important to `makemigrations` and `migrate` before running the app. This is done by

```
$ python manage.py makemigrations
$ python manage.py migrate
```

It is **recommended** that you also run the population script before.

```
$ python populate_connectercise.py
```

The app can be run using

```
$ python manage.py runserver
```

and then use a browser to go to http://127.0.0.1:8000/

### Running Tests
The test Python file is `connectercise\tests.py`. This file can be run using

```
$ python manage.py test
```

## Team Members
The following are the members of Lab 13 (Team B):
* [Marc Auf der Heyde](https://github.com/marcaufderheyde)
* [Inesh Bose](https://github.com/ineshbose)
* [Andrea Diaz Aguiar](https://github.com/2396765d)
* [Lok Hang Toby Lee](https://github.com/llhtoby)