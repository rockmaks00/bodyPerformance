## Требования:
```commandline
python 3.10.3
pip 22.0.4
```
## Первоначальная настройка и запуск:
Скачайте проект:
```commandline
git clone https://github.com/rockmaks00/bodyPerformance.git
```
В директории с проектом развернуть виртуальное окружение (проверьте версию интерпретатора python) и запустить его:
```commandline
python -m venv venv
venv\Scripts\activate.bat
```
После установите пакеты:
```commandline
pip install -r requirements.txt
```
Настройте переменные окружения: переименуйте файл `.env.example` в `.env` и внесите отсутствующие данные.

Запустите проект:
```commandline
python manage.py runserver
```