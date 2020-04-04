# Connectercise
This repository is for the WAD2 Team Project.

Connectercise is a web application in which users can connect with other users to do sport together. Users can add sports (which act like categories) and under each sport, there can be various requests, which are also created by the users.

## Using this Repository
This repository uses a virtual environment with specific packages, therefore it is essential to activate the environment and installing the packages before running the application.

```
$ git clone https://github.com/ineshbose/connectercise_project
$ cd connectercise_project
```

### Virtual Environment
If you haven't already created a virtual environment, you can do using Anaconda.

```
$ conda create -n connectercise python=3.8.0
$ conda activate connectercise
```

### Installing packages
A `requirements.txt` file mentions all the packages along with their versions used for this project. You can install them using:

```
(connectercise)$ pip install -r requirements.txt
```

### Running the App
The main Python file is `manage.py`. It is important to `makemigrations` and `migrate` before running the app. This is done by

```
(connectercise)$ python manage.py makemigrations
(connectercise)$ python manage.py migrate
```

It is **recommended** that you also run the population script before.

```
(connectercise)$ python populate_connectercise.py
```

The app can be run using

```
(connectercise)$ python manage.py runserver
```

and then use a browser to go to http://127.0.0.1:8000/

### Running Tests
The test Python file is `connectercise\tests.py`. It includes tests for models (`connectercise\models.py`), population script (`populate_connectercise.py`) and forms (`connectercise\forms.py`). This file can be run using

```
(connectercise)$ python manage.py test
```

## Assessment
This project counts for 40% of the final grade for the course. This is further divided into three parts.

### Design Specification
The design specification (a PDF providing a whole range of details regarding the design of the web application intended to implement) counts for 10% of the 40%. It is graded out of 20 marks and should include:

* an overview of the application
* user personas
* specifications i.e. minimal list of requirements
* a high-level system architecture diagram
* an ER diagram
* wireframes

### Presentation
The presentation counts for 5% of the 40%. It should include:

* a description of the design of the application, using some material from the design specification
* an overview of the technologies used
* a brief summary of the contributions of each team member
* a demonstration of the web application

**Note:** Due to COVID-19, this presentation was done in the form of a video.

### The Application / Project
The application / project is worth 25% of the 40%, graded out of 50 marks, and should be developed using Python, Django, HTML, CSS and associated technologies including JavaScript, JQuery and AJAX. The basic expectations include:

* the app should involve user authentication
* it should certainly interact with some kind of model stored in a database
* it should be visually appealing and have an intuitive user interface
* overall the functionality supported should be rich enough in order to demonstrate an understanding of the technologies listed above

## Developed With

* [Bootstrap](https://github.com/twbs/bootstrap): a CSS, JavaScript and HTML framework used to develop highly-responsive websites
* [Django](https://github.com/django/django): a web application framework written in Python
* [Django-Crispy-Forms](https://github.com/django-crispy-forms/django-crispy-forms): helps render and style forms in a neat and simple way
* [Django-Extensions](https://github.com/django-extensions/django-extensions): a collection of custom extensions for the Django Framework
* [Django-Location-Field](https://github.com/caioariede/django-location-field): a location field that supports maps and lets users pick locations
* [Django-Registration](https://github.com/ubernostrum/django-registration): provides user registration functionalities
* [JavaScript Libraries](static/js): some open-source JavaScript libraries that helped create this project; the files include URLs to the organisations
* [jQuery](https://github.com/jquery/jquery): a JavaScript library which simplifies programming operations
* [Pillow](https://github.com/python-pillow/Pillow): a fork of PIL (Python Imaging Library)

## Team Members
The following are the members of Lab 13 (Team B):
* [Marc Auf der Heyde](https://github.com/marcaufderheyde)
* [Inesh Bose](https://github.com/ineshbose)
* [Andrea Diaz Aguiar](https://github.com/2396765d)
* [Lok Hang Toby Lee](https://github.com/llhtoby)

<br /><hr><br />
More on [Behance](https://www.behance.net/gallery/93420701/Connectercise).