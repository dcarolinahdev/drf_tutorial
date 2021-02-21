# Tutorial DjangoRestFramework

_Quickstart django rest framework 3.12.2 with django 3.1.7 using python 3.8.5 on ubuntu 20.04_

1. Create the project directory

```
mkdir drf_tutorial
cd drf_tutorial
```

2. Create a virtual environment to isolate our package dependencies locally

```
python3 -m venv .env
source .env/bin/activate
```

3. Install Django and Django REST framework into the virtual environment

```
pip install django
pip install djangorestframework
pip install pygments

or __pip install requirements.txt__
```

4. Set up a new project with a single application

```
django-admin startproject tutorial
cd tutorial
python manage.py startapp snippets
```

5. Create superuser

```
python manage.py createsuperuser

Username: admin
Email address: admin@example.com
Password: pssw123.
```

6. Continue coding

- First create your models to work with
- then create serializer classes
- then create the views

Guided from [django-rest-framework](https://www.django-rest-framework.org/tutorial/1-serialization/)
