# Сервис бронирования переговорных комнат (Coworking Booking Service)

Этот REST API для бронирования переговорных комнат в коворкинге был сделан в рамках тестового задания в компанию "Shift" для курса Python.

## Используемые технологии

* Python 3.11
* FastAPI
* PostgreSQL 16
* SQLAlchemy 2.0
* Alembic
* JWT Authentication
* Docker
* Docker Compose
* Pytest

---

# Функциональность

## Аутентификация

Поддерживается вход пользователей по логину и паролю с выдачей JWT-токена.

Роли пользователей:

* `admin` — администратор
* `employee` — сотрудник

---

## Просмотр комнат

Получение списка доступных комнат.

Запрос:

```http
GET /rooms
```

Пример ответа:

```json
[
  {
    "id": 1,
    "name": "Room A",
    "description": "Large meeting room"
  },
  {
    "id": 2,
    "name": "Room B",
    "description": "Small meeting room"
  }
]
```

---

## Проверка доступности комнаты

Получение свободных временных слотов для выбранной комнаты на конкретную дату.

Запрос:

```http
GET /rooms/{room_id}/availability?date_value=2026-11-07
```

Формат даты:

```text
YYYY-MM-DD
```

Пример:

```text
2026-11-07
```

---

## Создание бронирования

Требуется JWT-токен.

Запрос:

```http
POST /bookings
```

Тело запроса:

```json
{
  "room_id": 1,
  "slot_id": 1,
  "booking_date": "2026-11-07"
}
```

---

## Мои бронирования

Получение списка бронирований текущего пользователя.

Запрос:

```http
GET /bookings/me
```

Требуется авторизация.

---

## Административный раздел

Получение списка всех бронирований.

Запрос:

```http
GET /admin/bookings
```

Параметры:

```text
limit
offset
```

Пример:

```http
GET /admin/bookings?limit=20&offset=0
```

Доступно только пользователям с ролью `admin`.

---

# Структура проекта

```text
app/
├── api/
│   ├── auth.py
│   ├── rooms.py
│   ├── bookings.py
│   └── admin.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   └── dependencies.py
│
├── models/
│   ├── user.py
│   ├── room.py
│   ├── slot.py
│   └── booking.py
│
├── repositories/
│   ├── booking_repository.py
│   ├── room_repository.py
│   └── user_repository.py
│
├── services/
│   ├── auth_service.py
│   ├── booking_service.py
│   └── room_service.py
│
├── schemas/
│   ├── auth.py
│   ├── booking.py
│   └── room.py
│
└── main.py

scripts/
└── seed.py

tests/
├── unit/
└── integration/

alembic/
Dockerfile
docker-compose.yml
```

---

# Тестовые данные

При запуске приложения автоматически создаются пользователи, комнаты и временные слоты.

## Пользователи

Администратор:

```text
Логин: admin
Пароль: admin123
```

Сотрудник:

```text
Логин: user
Пароль: user123
```

---

## Комнаты

### Room A

Временные интервалы:

```text
09:00–11:00
13:00–16:00
```

### Room B

Временные интервалы:

```text
09:00–12:00
14:00–18:00
```

---

# Запуск проекта

## Сборка Docker-образов

```bash
docker compose build --no-cache
```

---

## Запуск приложения

```bash
docker compose up
```

После запуска сервис будет доступен по адресу:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

OpenAPI Schema:

```text
http://localhost:8000/openapi.json
```

---

# Пример авторизации

## Получение JWT-токена

Запрос:

```http
POST /auth/login
```

Тело запроса:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Ответ:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

---

## Использование токена в Swagger

1. Выполнить запрос `/auth/login`.
2. Скопировать значение `access_token`.
3. Нажать кнопку **Authorize**.
4. Вставить:

```text
Bearer <jwt-token>
```

5. Подтвердить авторизацию.

После этого будут доступны защищённые эндпоинты.

---

# Работа с миграциями

Создание новой миграции:

```bash
alembic revision --autogenerate -m "migration_name"
```

Применение миграций:

```bash
alembic upgrade head
```

---

# Тестирование

## Запуск всех тестов

```bash
docker compose run --rm api poetry run pytest
```

---

## Запуск unit-тестов

```bash
docker compose run --rm api poetry run pytest tests/unit -v
```

---

## Запуск integration-тестов

```bash
docker compose run --rm api poetry run pytest tests/integration -v
```

---

## Запуск отдельного теста

```bash
docker compose run --rm api poetry run pytest tests/unit/test_security.py -v
```

---

# Реализованные тесты

## Unit-тесты

* Проверка создания `AuthService`
* Проверка создания `BookingRepository`
* Проверка хеширования пароля
* Проверка верификации пароля

## Integration-тесты

* Проверка доступности health endpoint
* Фикстура TestClient
* Базовая проверка существования login endpoint

---

# Реализованные требования

В рамках задания реализовано:

* Docker Compose инфраструктура
* PostgreSQL база данных
* Alembic миграции
* JWT-аутентификация
* Ролевая модель доступа
* Просмотр комнат
* Проверка доступности слотов
* Создание бронирований
* Получение собственных бронирований
* Административный просмотр бронирований
* Разделение на Repository / Service / API слои
* Seed-данные для демонстрации работы системы
* Unit и Integration тесты
* Swagger-документация API



