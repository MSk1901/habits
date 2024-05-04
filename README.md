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
#### 2. Перейдите в директорию проекта, создайте виртуальное окружение и установите зависимости:
```
cd habits
```
- pip
```
python3 -m venv venv
```
```
pip install -r requirements.txt
```
- poetry
```
poetry init
```
```
poetry install
```
#### 3. Настройте переменные окружения: 

   1. Создайте файл `.env` в корневой директории 
   2. Скопируйте в него содержимое файла `.env.sample` и подставьте свои значения

#### 4. Создайте и примените миграции:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
</details>

<details>
<summary>Использование</summary>

#### 1. Запустите сервер разработки:
```
python3 manage.py runserver
```
Откройте браузер и перейдите по адресу http://127.0.0.1:8000/ или http://localhost:8000/

#### 2. Административная панель:
1. Для доступа к админке создайте суперпользователя
```
python3 manage.py csu
```
2. Откройте администратичную панель по адресу http://127.0.0.1:8000/admin/ или http://localhost:8000/admin/
   - Введите e-mail и пароль
   - Данные для входа находятся в файле `/users/management/commands/csu.py`. При желании, вы можете задать свои e-mail и пароль и заново выполнить команду
          
#### 3. Настройка уведомлений в Telegram:
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
#### 4. Создание привычки:
1. Получите `Bearer token` созданного пользователя по адресу http://127.0.0.1:8000/users/login/
2. Для создания привычки перейдите по адресу http://127.0.0.1:8000/users/register/
3. Укажите токен в заголовке запроса
4. Укажите поля в теле запроса в формате `json`:
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
     
#### 5. Другие способы взаимодействия:
Все способы взаимодействия вы можете найти в документации
</details>

## Документация
Документация по API доступна по адресам:
- Swagger - http://127.0.0.1:8000/docs/
- Redoc - http://127.0.0.1:8000/redoc/



Автор проекта Мария Кузнецова - [kuznetsova19.m@gmail.com](mailto:kuznetsova19.m@gmail.com)
