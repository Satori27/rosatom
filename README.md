# rosatom


## Описание

В API доступны и работают функции регистрации логина и выхода из аккаунта, чтобы чатом было пользоваться удобно я добавил в него веб-интерфейс. Есть возможность писать сообщения другим пользователям. Есть админ-панкль и написаны тесты. В качестве БД использовал postgres, все запросы с БД работают асинхронно. Также все упаковано в docker и можно запустить сервер с помощью docker-compose

## Запуск проекта

Для запуска приложения используйте Docker Compose.

1. **Клонируйте репозиторий:**

    ```sh
    git clone https://github.com/Satori27/rosatom.git
    cd rosatom
    ```

2. **Запустите приложение с помощью Docker Compose:**

    ```sh
    docker compose up
    ```

Команда запустит контейнер web и pg. Приложение будет доступно по адресу:

     http://localhost:10301

В самом контейнере открыт порт `:8000`


## User Interface
Интерфейс регистрации особенно ничем не отличается от стандартного процесса регистрации.
Для того чтобы начать чатиться, нужно для начала зарегестрироваться. После успешной регистраии нужно залогиниться под тем же email. После успешной авторизации, вам будут доступны все пользователи сервиса. Можете выбрать лубого юзера и начать чатиться.

## Тесты
Для тестов, я создал отдельное окружение, чтобы выполнение тестов не мешало работе основного приложения. Тесты я написал в виде табличных тестов. Для запуска тестового окружения используйте:
```sh
docker compose -f test-docker-compose.yaml up -d
```

А для запуска самих тестов:
```sh
docker exec -it test-web pytest
```

## Админ панель
Чтобы открыть админ панель, нужно залогиниться через `ADMIN_EMAIL` и `ADMIN_PASSWORD`, которые указаны в .env файле и перейти по ссылке   http://localhost:10301/admin . (Админа регистрировать не надо, он уже зарегестрирован).Для админа доступны все чаты, также нажав на определенный чат - админ может нажать на кнопку заблокировать "username" в верхней панели. 

## Итог

В общем, я реализовал все основные и дополнительные требования. Было очень интересно разрабатывать свой чат. Благодаря этому тестовому я узнал, что такое websocket о его преимуществах и недостатках, и получил опыт работы с ним. Также познакомился с такими технологиями как alembic, FastAPI и научился работать с sqlalchemy и PostgreSQL асинхронно.