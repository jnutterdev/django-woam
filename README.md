Django site using Tailwind and HTMX

When installing, run: 

To get started, create python virtualenv, ex:
`pip install pipenv` (if not already installed)
`pipenv install`
`pipenv shell`

Create a .env file for storing the Django secret key:
`touch .env` 

You can also use the following script to generate a new secret key: 
`./generate_secret.py`

Install django-tailwind:
`./manage.py tailwind install`

Run django's server:
`./manage.py runserver`

In another terminal window, run Tailwind server:
`./manage.py tailwind start`