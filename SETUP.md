## Initial Setup Instructions

1. [Follow the instructions here to create and activate a virtual env called venv](http://flask.pocoo.org/docs/1.0/installation/)

Do the steps up until "Install Flask".

2. Upgrade pip
`python3 -m pip install --upgrade pip`

3. Install requirements
`pip install -r requirements.txt`

4. Tell Flask how to import the app
`export FLASK_APP=emojify.py`

5. Run the app
`flask run`

## Installing additional flask extensions/Python packages

If you install a Flask extension, update requirements.txt by installing pipreqs:

`pip install pipreqs`

and running the following command from the top-level project directory:

`pipreqs . --ignore emojify_poc`
