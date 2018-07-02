## Initial Setup Instructions

1. [Follow the instructions here to create and activate a virtual env called venv](http://flask.pocoo.org/docs/1.0/installation/)

Do the steps up until "Install Flask".

2. Upgrade pip
`python3 -m pip install --upgrade pip`

3. Install requirements
`pip install -r requirements.txt`

4. Install dotenv `pip install python-dotenv`

5. Tell Flask how to import the app
`export FLASK_APP=emojify.py`

6. Create the database:
`flask db init`

7. Run migrations:
`flask db upgrade`

8. Run the app:
`flask run`

## Development

**Important:**

Whenever you are developing locally, you will want to start your virtual environment by running  `. venv/bin/activate` before doing any other steps.

You also may want to run `flask db upgrade` if any db migrations have been added.

Any changes to models should be followed up by a `flask db migrate` and a `flask db upgrade`. Undo a migration by running `flask db downgrade`.

Run a python shell with the app context by running `flask shell`.

## Installing additional flask extensions/Python packages

If you install a Flask extension, update requirements.txt by installing pipreqs:

`pip install pipreqs`

and running the following command from the top-level project directory:

`pipreqs . --ignore emojify_poc`
