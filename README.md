# Icemint test task

To install everything you need execute this in terminal:
```sh
git clone https://github.com/true-datura/IcemintTest
cd IcemintTest
virtualenv -p python3 .fenv
. .fenv/bin/activate
pip install -r requirements.txt
cd icemint_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Now you can see the blog at `127.0.0.1:8000`.
