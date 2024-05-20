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
#### 2. Navigate to the project root directory
#### 3. Set up environment variables:

   1. Create a file named `.env` in the root directory
   2. Copy the contents of the `.env.sample` file into it and replace the values with your own
   3. For the project to work correctly in the local development environment, set the value of `DEBUG=True` to automatically handle static files and provide detailed error messages.


#### 4. Run the command to build and start Docker containers:
```
docker-compose up -d --build
```
</details>

<details>
<summary>Usage</summary>

#### 1. Admin Panel:
To access the admin panel, create a superuser

1. You will need to view the list of running containers and copy the container id of the app container
    ```
    docker ps
    ```
    Example output:
    ```
    CONTAINER ID   IMAGE                                                         
    e5e38dccec3d   drf-lms-app                
    ```
2. Then execute the command to enter the container and execute commands available in its environment
    ```
    docker exec -it <container id> bash
    ```
3. To create a superuser (admin), execute the command
    ```
    python3 manage.py createsuperuser
    ```
   You can view the superuser's email and password for logging into the admin panel in the `/users/management/commands/csu.py` file. If desired, you can set your own email and password.


4. Open the administrative panel at http://localhost:8000/admin/ and enter the email and password of the superuser
          
#### 2. Setting up Telegram notifications:
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
#### 3. Creating a habit:
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

#### 4. Other interaction methods:
You can find all interaction methods in the documentation
</details>

## Documentation
API documentation is available at:
- Swagger - http://127.0.0.1:8000/docs/
- Redoc - http://127.0.0.1:8000/redoc/



Project Author: Maria Kuznetsova - [kuznetsova19.m@gmail.com](mailto:kuznetsova19.m@gmail.com)
