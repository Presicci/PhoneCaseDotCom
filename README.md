clone then execute:\
python manage.py collectstatic\
python manage.py makemigrations\
python manage.py migrate

dependencies:\
python -m pip install django~=4.1.0\
python -m pip install 'environs[django]==9.5.0'

to run:\
python manage.py runserver

to created admin user:\
python manage.py createsuperuser