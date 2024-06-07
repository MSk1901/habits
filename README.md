## API Трекера привычек
**Backend-часть веб-приложения для трекинга привычек.**
- Просмотр публичных привычек
- Просмотр и добавление своих привычек
- Напоминания в Telegram о привычках
### Стек технологий:
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

## Содержание

<details>
<summary>Инструкция по развертыванию проекта</summary>

#### 1. Клонируйте проект:
```
git clone https://github.com/MSk1901/habits.git
```
#### 2. Перейдите в корневую директорию проекта 
#### 3. Настройте переменные окружения: 

   1. Создайте файл `.env` в корневой директории 
   2. Скопируйте в него содержимое файла `.env.sample` и подставьте свои значения
   3. Для корректной работы проекта в локальной среде разработки установите значение `DEBUG=True`, чтобы обеспечить автоматическую обработку статических файлов и подробные сообщения об ошибках.


#### 4. Запустите команду для сборки и запуска контейнеров Docker:
```
docker-compose up -d --build
```
</details>

<details>
<summary>Использование</summary>

#### 1. Административная панель:
Для доступа к админке создайте суперпользователя

1. Для этого нужно будет посмотреть список запущенных контейнеров и скопировать id контейнера app
    ```
    docker ps
    ```
    Пример вывода:
    ```
    CONTAINER ID   IMAGE                                                         
    e5e38dccec3d   drf-lms-app                
    ```
2. После этого выполните команду, чтобы попасть в контейнер и выполнять команды, доступные в его окружении
    ```
    docker exec -it <id контейнера> bash
    ```
3. Для создания суперпользователя (админа) выполните команду
    ```
    python3 manage.py csu
    ```
   E-mail и пароль суперпользоветеля для входа в админку вы можете посмотреть в файле `/users/management/commands/csu.py`. При желании, вы можете задать свои e-mail и пароль


4. Откройте администратичную панель по адресу http://localhost:8000/admin/ и введите e-mail и пароль суперпользоветеля
          
#### 2. Настройка уведомлений в Telegram:
1. Для отправки уведомлений у пользователя должно быть заполнено поле `chat_id`. Значение - id чата в Telegram.
2. Поле можно заполнить:
   - При регистрации.
     Для этого перейдите по адресу http://127.0.0.1:8000/users/register/ и заполните все поля. Пример заполнения в формате `json`:
        ```
        {
            "email": "user@example.com",
            "password": "Somepassword",
            "chat_id": "000000001"
        }
        ```
   - В административной панели.
     Заполните нужное поле при создании или редактировании пользователя
#### 3. Создание привычки:
1. Получите `Bearer token` созданного пользователя по адресу http://127.0.0.1:8000/users/login/
2. Для создания привычки перейдите по адресу http://127.0.0.1:8000/habits/
3. Укажите токен в заголовке запроса
4. Укажите поля в теле запроса в формате `json` и отправьте `POST` запрос:
      ```
      {
          "place": "Дома",
          "time": "20:00",
          "action": "Съесть овощи за ужином",
          "is_enjoyable": false,
          "periodicity": 1, # Периодичность привычки, например, раз в день
          "treat": "Съесть любимый десерт",
          "duration": "00:01:00", # Длительнось выполнения привычки в формате ЧЧ:ММ:СС
          "is_public": true
      }
      ```
     
#### 4. Другие способы взаимодействия:
Все способы взаимодействия вы можете найти в документации
</details>

## Документация
Документация по API доступна по адресам:
- Swagger - http://127.0.0.1:8000/docs/
- Redoc - http://127.0.0.1:8000/redoc/



Автор проекта Мария Кузнецова - [kuznetsova19.m@gmail.com](mailto:kuznetsova19.m@gmail.com)
