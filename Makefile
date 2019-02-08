server:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

test:
	python manage.py test

load_fixtures:
	python manage.py loaddata */fixtures/*.json

startapp:
	python manage.py startapp

help:
	@echo "\x1b[32;01m"make server "\x1b[30;01m" '-->' to start the server
	@echo "\x1b[32;01m"make migrate "\x1b[30;01m" '-->' to migrate
	@echo "\x1b[32;01m"make migrations "\x1b[30;01m" '-->' to make migrations
	@echo "\x1b[32;01m"make startapp "\x1b[30;01m" '-->' to start apps
	@echo "\x1b[32;01m"make help "\x1b[30;01m" '-->' to see a list of all commands
