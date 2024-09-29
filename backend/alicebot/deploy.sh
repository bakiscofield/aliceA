git add ../../
git commit -m "Fix then"
git pull origin main
pip install -r requirements.txt
rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
python3 manage.py runscript factory
python manage.py createsuperuser
python manage.py collectstatic
python3 manage.py runserver
