
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

Для запуска основго скрипта нужно прописать команду в терминале `python3 app.py`