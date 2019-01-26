#!/bin/bash

#NOTE: project structure courtesy of https://camillovisini.com/barebone-serverless-flask-rest-api-on-zeit-now/

# setup project folder
cd ~/PycharmProjects
mkdir barebone-serverless-flask-api-zeit-now
cd barebone-serverless-flask-api-zeit-now

# setup virtual environment
python3 -m venv my_virtual_environment
source my_virtual_environment/bin/activate
pip3 install flask flask-restplus Flask-SQLAlchemy psycopg2
pip3 freeze > requirements.txt
deactivate

# setup project structure and open in PyCharm
touch now.json index.py
charm .