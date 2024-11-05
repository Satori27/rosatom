# rosatom


## Функциональность

В API доступны и работают функции регистрации логина и выхода из аккаунта, для удобного взаимодействия чатом можно пользоваться через веб-интерфейс. Есть возможность писать сообщения другим пользователям. Есть администратор и написаны тесты. В качестве БД использовал postgres, запросы работают асинхронно. Также все упаковано в docker и можно запустить сервер одной командой

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

Команда запустит контейнер backend. Приложение будет доступно по адресу:

     http://localhost:10301

В самом контейнере открыт порт `:8000`

## Тесты
Для тестов, я создал отдельное окружение, чтобы выполнение тестов не мешало работе основного приложения. Для запуска тестового окружения используйте:
```sh
    docker compose -f test-docker-compose.yaml up -d
```