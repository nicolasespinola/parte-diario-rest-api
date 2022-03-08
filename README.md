# parte-diario-rest-api

Rest api para parte diario

## Requerimientos

- Python >= 3.7
- Pipenv
- MySQL >= 5.6

## Entorno de desarrollo

1. Crea una base de datos para el proyecto:

    ```bash
    mysql --execute="CREATE DATABASE parte-diario-rest-api;"
    mysql --execute="CREATE USER 'parte-diario-rest-api'@'localhost' identified by 'superstrongpassword';"
    mysql --execute="GRANT ALL PRIVILEGES ON parte-diario-rest-api.* to 'parte-diario-rest-api'@'localhost';"
    ```

2. En la carpeta raíz, crea un archivo llamado `env.json` con el siguiente contenido:

    ```json
    {
        "debug": true,
        "secret_key": "supersecretkey",
        "allowed_hosts": ["*"],
        "db_user": "parte-diario-rest-api",
        "db_password": "superstrongpassword",
        "db_name": "parte-diario-rest-api",
        "db_host": "127.0.0.1",
        "db_port": 3306
    }
    ```

3. Instala las dependencias del proyecto:

    ```bash
    pipenv install
    ```

4. Ejecuta las migraciones y crea un superusuario:

    ```bash
    pipenv run python manage.py migrate
    pipenv run python manage.py createsuperuser
    ```

5. Ejecuta el servidor de desarrollo:

   ```bash
   pipenv run python manage.py runserver
   ```
