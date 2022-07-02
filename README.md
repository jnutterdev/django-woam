# This is more of a practice project at the moment to refresh my memory and see how a fullstack Django application would work with different frontends. The backend currently runs on Django/Django REST framework to serve up an API. For the frontend, there's currently two different versions being served: Tailwind and HTMX on :8000, and then on :3000, React. 

To get started, create python virtualenv, ex:
`pip install pipenv` (if not already installed)
`pipenv install`
`pipenv shell`

Create a .env file for storing the Django secret key:
`touch .env` 

You can also use the following script to generate a new secret key: 
`./generate_secret.py`

Generate a user for Django: 
`./manage.py createsuperuser`

### For Tailiwind on :8000
Install django-tailwind:
`./manage.py tailwind install`

Run django's server:
`./manage.py runserver`

In another terminal window, run Tailwind's preprocessor:
`./manage.py tailwind start`

### For React on :3000
`cd frontend/`
`npm install`
`npm run start`

### Perform CRUD operations to create blog posts using Django REST API on :8000
`http://localhost:8000/api/posts/`