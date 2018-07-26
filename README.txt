Label Automobile
================

Getting Started
---------------

- Change directory into your newly created project.

    cd label_automobile

- Create a Python virtual environment.

    python3 -m venv env

- Activate virtual environment
    source env/bin/activate

- Upgrade packaging tools.

    pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Change your settings
    development.ini -> Database settings and possibly application port

- Configure the database.

    init_mob_db development.ini

- Add test data to the database

    mock_mob_db development.ini

---- Not implemented yet
- Run your project's tests.

    pytest

- Run your project.

    pserve development.ini (--reload optional to reload on code changes)
