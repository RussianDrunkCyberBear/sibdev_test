# overview

Test exersise. Simple site parser with database and choosable time dealay for url request<br />
tested with python 3.7.4<br />
uses sqlite wich installing with django by defaul<br />



# for using with virtual enviroment

pip install virtualenv<br />
python -m venv env<br />
	
linux: source env/bin/activate<br />
or<br />
win: env\Scripts\activate<br />



# installation

pip install -r requirements.txt<br />
python manage.py makemigrations<br />
python manage.py migrate<br />
python manage.py createsuperuser 	# admin login password create<br />



# start server
python manage.py runserver<br />