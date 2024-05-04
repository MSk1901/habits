## Habits Tracker API
**Backend part of a web application for habit tracking.**
- Viewing public habits
- Viewing and adding your own habits
- Telegram reminders about habits
### Technology Stack:
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.4-blue?logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15.1-blue)](https://www.django-rest-framework.org/)
[![Celery](https://img.shields.io/badge/Celery-5.4.0-blue?logo=Celery)](https://docs.celeryq.dev/en/stable/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-5.0.4-blue?logo=Redis)](https://redis.io/)

- `python`
- `django`
- `djangorestframework`
- `celery`
- `celery-beat`
- `postgreSQL`
- `redis`

## Table of Contents

<details>
<summary>Deployment Guide</summary>

#### 1. Clone the project:
```
git clone https://github.com/MSk1901/habits.git
```
#### 2. Navigate to the project directory, create a virtual environment and install dependencies:
```
cd habits
```
- Using pip
```
python3 -m venv venv
```
```
pip install -r requirements.txt
```
- Using poetry
```
poetry init
```
```
poetry install
```
#### 3. Set up environment variables: 

   1. Create a `.env` file in the root directory 
   2. Copy the contents of the `.env.sample` file into it and replace with your values

#### 4. Create and apply migrations:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
</details>

<details>
<summary>Usage</summary>

#### 1. Run the development server:
```
python3 manage.py runserver
```
Open your browser and go to http://127.0.0.1:8000/ or http://localhost:8000/

#### 2. Administrative Panel:
1. To access the admin panel, create a superuser:
```
python3 manage.py csu
```
2. Open the administrative panel at http://127.0.0.1:8000/admin/ or http://localhost:8000/admin/
   - Enter your email and password
   - Login credentials are located in the `/users/management/commands/csu.py` file. If desired, you can set your own email and password and re-run the command
          
#### 3. Setting up Telegram notifications:
1. To send notifications, the user's `chat_id` field must be filled. The value is the chat id in Telegram.
2. The field can be filled in:
   - During registration.
     To do this, go to http://127.0.0.1:8000/users/register/ and fill in all the fields. Example format for filling in JSON:
        ```
        {
            "email": "user@example.com",
            "password": "Somepassword",
            "chat_id": "000000001"
        }
        ```
   - In the administrative panel.
     Fill in the required field when creating or editing a user
#### 4. Creating a habit:
1. Obtain the `Bearer token` of the created user at http://127.0.0.1:8000/users/login/
2. To create a habit, go to http://127.0.0.1:8000/users/register/
3. Specify the token in the request header
4. Specify fields in the request body in JSON format:
      ```
      {
          "place": "Home",
          "time": "20:00",
          "action": "Eat vegetables for dinner",
          "is_enjoyable": false,
          "periodicity": 1, # Habit frequency, for example, once a day
          "treat": "Eat favorite dessert",
          "duration": "00:01:00", # Habit duration in HH:MM:SS format
          "is_public": true
      }
      ```

#### 5. Other interaction methods:
You can find all interaction methods in the documentation
</details>

## Documentation
API documentation is available at:
- Swagger - http://127.0.0.1:8000/docs/
- Redoc - http://127.0.0.1:8000/redoc/



Project Author: Maria Kuznetsova - [kuznetsova19.m@gmail.com](mailto:kuznetsova19.m@gmail.com)
