### Проект API Yatube (v1) предоставляет доступ к данным через API
 

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/SL010/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Прочесть документацию к API проекта Yatube (v1) http://127.0.0.1:8000/redoc/
```

Установить основные библиотеки
Django==3.2.16
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
```

Автор: [Борисов Вячеслав]
(https://github.com/SL010)
Почта: borisov.slava00@yandex.ru

