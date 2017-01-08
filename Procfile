web: gunicorn curriculum.wsgi --log-file -
web: python curriculum/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT curriculum/settings.py
