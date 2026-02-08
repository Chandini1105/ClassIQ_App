Preview and Run

Quick steps to run locally for review:

```bash
# setup virtual environment (Windows example)
python -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# create superuser (optional)
python manage.py createsuperuser

# run the development server
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser. Login with admin or created user to see the dashboard and updated corporate styles.