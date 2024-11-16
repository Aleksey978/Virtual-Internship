# Pereval API

Этот проект представляет собой REST API для управления данными о перевалах (горных переходах) с использованием FastAPI и PostgreSQL. API позволяет создавать, получать, обновлять и удалять записи о перевалах.

## Оглавление

- [Технологии](#технологии)
- [Использование](#использование)




## Технологии

- **FastAPI**: Основная библиотека для создания API.
- **SQLAlchemy**: ORM (Object-Relational Mapping) для работы с базой данных.
- **Psycopg2-binary**: Драйвер для подключения к PostgreSQL.
- **Pydantic**: Библиотека для валидации данных.
- **PostgreSQL**: Реляционная база данных.

## Использование


POST /perevals/ - Создание нового перевала.

GET /perevals/{pereval_id} - Получение информации о конкретном перевале по его ID.

PATCH /perevals/{pereval_id} - Обновление информации о существующем перевале, если он в статусе new.

GET /perevalData/?user__email= - Получение списка перевалов, отправленных пользователем с указанным email.


Примеры запросов:
Создание нового перевала:

```curl -X POST "http://localhost:8000/perevals/" -H "Content-Type: application/json" -d'```

```
{

"beauty_title": "пер. ",
  
  "title": "Пхия",
  
  "other_titles": "Триев",
  
  "connect": "",
  
  "add_time": "2021-09-22 13:18:13",
  
  "user": {
  
    "email": "example@example.com",
    
    "fam": "Пупкин",

    "name": "Василий",
    
    "otc": "Иванович",
    
    "phone": "+7 555 55 55"
    
  },
  
  "coords": {
  
    "latitude": 45.3842,
    
    "longitude": 7.1525,
    
    "height": 1200
    
  },
  
  "level": {
  
    "winter": "",
    
    "summer": "1А",
    
    "autumn": "1А",
    
    "spring": ""
    
  },
  
  "images": [
  
    {
    
      "data": "<картинка1>",
      
      "title": "Седловина"
      
    },
    
    {
    
      "data": "<картинка>",
      
      "title": "Подъём"
      
    }
    
  ]
  
}
'

```



Получение информации о перевале по ID:

```curl -X GET "http://localhost:8000/perevals/1"```

Обновление информации о перевале:


```curl -X PATCH "http://localhost:8000/perevals/1" -H "Content-Type: application/json" -d '```

```
{

  "beauty_title": "пер. ",
  
  "title": "Пхия",
  
  "other_titles": "Триев",
  
  "connect": "",
  
  "add_time": "2021-09-22 13:18:13",
  
  "user": {
  
    "email": "example@example.com",
    
    "fam": "Пупкин",

    "name": "Василий",
    
    "otc": "Иванович",
    
    "phone": "+7 555 55 55"
    
  },
  
  "coords": {
  
    "latitude": 45.3842,
    
    "longitude": 7.1525,
    
    "height": 1200
    
  },
  
  "level": {
  
    "winter": "",
    
    "summer": "1А",
    
    "autumn": "1А",
    
    "spring": ""
    
  },
  
  "images": [
  
    {
    
      "data": "<картинка1>",
      
      "title": "Седловина"
      
    },
    
    {
    
      "data": "<картинка>",
      
      "title": "Подъём"
      
    }
    
  ]
  
}'

```

Получение списка перевалов по email пользователя:

```curl -X GET "http://localhost:8000/perevalData/?user__email=example@example.com"```
