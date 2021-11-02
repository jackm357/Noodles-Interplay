# Database Setup (PostreSQL)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Django DB Setup](https://docs.djangoproject.com/en/3.2/intro/tutorial02/)
- [PostgreSQL & Django Integration Example](https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django)
## Initial Setup
1. Download PostgreSQL: https://www.postgresql.org/download/
2. PostgreSQL Server <interplay_db> and database <interplay_db> created in pgAdmin with:
    - user: postgres
    - password: noodle$21
    - port: 5432
    - host: localhost
3. Install dependencies - in work environment, use command:
    ```
    $ pip install psycopg2
    ```
    or, if you encounter issues:
    ```
    $ pip install psycopg2-binary
    ```
4. Update settings.py:
   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'interplay_db',
           'USER': 'postgres',
           'PASSWORD': 'noodle$21',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
   and migrate changes with:
   ```
   $ python manage.py migrate
   ```
5. Django is now set up with PostgreSQL as default DB.
   - Superuser: noodles_admin
   - Password: noodle$21

