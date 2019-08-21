# overview

Test exersise. Simple site parser with database and choosable time dealay for url request
tested with python 3.7.4
uses sqlite wich installing with django by defaul



# for using with virtual enviroment

pip install virtualenv
python -m venv env
	
linux: source env/bin/activate
or
win: env\Scripts\activate



# installation

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 	# admin login password create



# start server
python manage.py runserver