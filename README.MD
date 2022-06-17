
# Flask скрипт для получения данных с документа Google Sheets, при помощи Google API в онлайн режиме

## Предварительная подготовка

1. Скачать на ПК интерпретатор языка Python (версии 3.9 или новее).
2. Желательно поставить виртаульное окружение в директории проекта:
   * `python3 -m venv name`
3. Следом, надо активировать окружение:
   * Windows `.\env\Scripts\activate`
   * Linux/MacOS `source env/bin/activate`
4. Установить необходимые библиотеки с помощью команды:
   * `python3 -m pip install -r requirements.txt`
5. Установить PostgreSQL на ПК
   * [Установка PostgreSQL на Mac](https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/)
   * [Установка PostgreSQL на Windows](https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm)
   * [Установка PostgreSQL на Linux](https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL_Linux.htm)
6. Создать пользователя и базу данных PostgreSQL
   * [Гайд по созданию пользователя и базы данных PostgreSQL](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)
7. Создать файл **config.py** и прописать пользователя, пароль и название БД (Пример *config.py.default*)
   ```python
   POSTGRESQL = {
    'pguser': 'changeme',
    'pgpasswd': 'changeme',
    'pghost': 'localhost',
    'pgport': 5432,
    'pgdb': 'changeme'
   }
---

## Запуск скрипта

### Простой запуск

Для начала нужно перейти в директорию приложения `cd src`

Затем запустить скрипт через консоль `python3 app.py`

После перехода на `http://localhost:5001/` приложение начнёт свою работу

### Запуск через Docker

1. Зайти в файл `docker-compose.yml` и прописать в поля __POSTGRES_DB__, __POSTGRES_USER__, __POSTGRES_PASSWORD__ название БД, имя пользователя и пароль PostgreSQL
2. Прописать в командной строке `docker-compose up`


---

## Дополнительно

### Запуск Telegram оповещения о сроках поставки

Чтобы запустить __Telegram__ оповещения
  * В `bot.py` ввести Token своего бота Telegram. Подробнее: https://core.telegram.org/bots
  * Ввести ID пользователя которому должны приходить оповещения. Подробнее: [Telegram ID](https://perfluence.net/blog/article/kak-uznat-id-telegram#:~:text=Telegram%20user%20ID%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D1%86%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%BE%D0%B9,%D0%B2%20%D0%BC%D0%B5%D0%BD%D1%8E%20%D0%BC%D0%B5%D1%81%D1%81%D0%B5%D0%BD%D0%B4%D0%B6%D0%B5%D1%80%D0%B0%20%D0%BD%D0%B5%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%D1%81%D1%8F.)
```python
   TOKEN = 'Your token'
   
   bot = telebot.TeleBot(TOKEN)
   
   user_id_to_send: int = 'user id'