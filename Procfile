web: gunicorn --bind 0.0.0.0:${PORT} manage:app
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade