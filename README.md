# gp-Storage-Auditor
Автоматическое администрирование Greenplum, которое помогает находить тяжелые таблицы и аномалии в распределение данных. Скрипт подключается к базе, собирает статистику  по указанным таблицам и генерирует отчет в Markdown.


## Quickstart

1. Перед запуском создайте файл .env в корне проекта, опираясь на .env.example: 
```ini
GP_HOST=localhost
GP_PORT=5432
GP_DB=postgres
GP_USER=your_user
GP_PASSWORD=your_pass
TARGET_TABLES=public.sales,public.users
```
2. Соберите образ:
```ini
docker build -t gp-auditor .
```
3. Запустите:
```
docker run --rm --env-file .env -v $(pwd):/app gp-auditor
```
4. После выполнение появится файл report.md.

## Локальный запуск 

1. Установите зависимотси:

```
pip install -r requirements.txt
```
2. Запустите модуль:
```
python -m src.main
```