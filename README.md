# Restaurant-Kitchen-Service

Django project for managing dish types, dishes and cooks in Restaurant Kitchen Service

## Check it out!

[Restaurant Kitchen Service deployed to render.com](https://restaurant-kitchen-service-j3d2.onrender.com)

## Installation

Python must be already installed


```bash
git clone https://github.com/roma-mechanic/Restaurant-Kitchen-Service
cd Restaurant-Kitchen-Service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```
Fill in the .env file with user data according to the .env_sample file

```bash
python manage.py runserver
```

## Features

* Authentication functionality for Cook/User
* Managing dish types, dishes and cooks directly from website interface
* Powerful interfaces, admin panel for advanced management


## Project scheme

![Project scheme](/static/assets/img/project_scheme.png)

## Demo

![Demo](/static/assets/img/demo.png)
