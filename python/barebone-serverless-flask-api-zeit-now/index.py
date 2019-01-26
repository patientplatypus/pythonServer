

from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
import json
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
with app.app_context():

  from routes import *

  if __name__ == '__main__':
    app.run(debug=True)
