Welcome to the Python week microsite

Find below the instructions to make it work:

- Download the repo
- In the project terminal run pipenv shell
- Install flask, cors, gunicorn & werkzeug
- In Pipfile you will find all the technologies added to the repo and most importantly the scripts to run this programme
- In your terminal, run 'pipenv run dev' to use the basic server
- In your terminal, run 'pipenv run start' to use WSGI


This is a basic microsite with 3 endpoints:

- Home (displays a welcome message)
- Skills (displays the current skills that our students have learnt)
- Future (displays the skills that students will acquire during the Python LAP)

Extras:

- We are using werkzeug to raise personalised exceptions
- We have installed gunicorn to implement wsgi (in case our project grows and needs to manage more requests)
- We are using CORS to avoid CORS errors


