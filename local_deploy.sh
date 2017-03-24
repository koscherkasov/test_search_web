source venv/bin/activate
export APP_SETTINGS='config.DevelopmentConfig'
export PYTHONPATH=`pwd`
python manage.py runserver